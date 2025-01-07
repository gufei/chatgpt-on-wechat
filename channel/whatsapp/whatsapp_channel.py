import json
import urllib.parse
import requests
import web

from bridge.context import Context, ContextType
from channel.chat_channel import ChatChannel
from channel.wechat.wxhook_message import WxHookMessage
from channel.whatsapp.whatsapp_message import WaHookMessage
from common.expired_dict import ExpiredDict
from common.log import logger
from config import conf
from bridge.reply import Reply, ReplyType
from alibabacloud_cams20200606.client import Client as cams20200606Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cams20200606 import models as cams_20200606_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class WaHookChannel(ChatChannel):
    groups = dict()
    nickNames = dict()
    users = dict()

    def __init__(self):
        super().__init__()
        # 历史消息id暂存，用于幂等控制
        self.receivedMsgs = ExpiredDict(60 * 60 * 7.1)
        config = open_api_models.Config(
            # Required, please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID is set.,
            access_key_id='',
            # Required, please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_SECRET is set.,
            access_key_secret=''
        )
        # See https://api.alibabacloud.com/product/cams.
        config.endpoint = f'cams.ap-southeast-1.aliyuncs.com'
        self.client: cams20200606Client = cams20200606Client(config)

    def whatsapp_request(self, from_, to, text):
        send_chatapp_message_request = cams_20200606_models.SendChatappMessageRequest(
            type='message',
            message_type='text',
            channel_type='whatsapp',
            from_=from_,
            to=to,
            content='{"text": "' + text + '", "link": "", "caption": "", "fileName": "" }',
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = self.client.send_chatapp_message_with_options(send_chatapp_message_request, runtime)
            logger.debug(f"[whatsapp_request] resp: {UtilClient.to_jsonstring(resp)}")
            return resp
        except Exception as e:
            logger.error(f"[whatsapp_request] send message failed, error: {e}")
            return None

    def startup(self):
        # 启动回调监听
        urls = (
            '/robot-api/whatsapp/receiveChatBotMsg', 'channel.wechat.wxhook_channel.WaHookController'
        )
        app = web.application(urls, globals(), autoreload=False)
        web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 0))

    def send(self, reply: Reply, context: Context):
        fromid = context["fromid"]
        if reply.type == ReplyType.TEXT:
            res = self.whatsapp_request(fromid, context["receiver"], reply.content)
            context["is_success"] = res.body.code



class WaHookController:
    FAILED_MSG = '{"success": false}'
    SUCCESS_MSG = '{"success": true}'

    wainfos = dict()

    def get_wainfo_by_phone(self, phone):
        from app import db_storage
        wainfo = db_storage.get_info_by_wxid(phone)
        if wainfo is None:
            return None
        else:
            return wainfo

    def POST(self):
        data = json.loads(web.data().decode("utf-8"), strict=False)
        logger.info(f"[wx_hook] receive request: {data}")

        channel = WaHookChannel()
        # 更正连接信息
        wainfo = self.get_wainfo_by_phone(data.get("From"))

        channel.user_id = data.get("To")

        if wainfo is not None:
            channel.name = wainfo['nickname']

        # if "cmdId" in msg and msg.get("msgtype") not in ["1", "34"]:
        #     return "this is a cmd message"
        selfwxid = data.get("From")

        # 只处理文本类型的消息
        # if msg.get("msgtype") not in ["1", "34"]:
        #     logger.debug(f"[wx_hook] not a text message, msgtype={msg.get('msgtype')}")
        #     continue

        # if channel.receivedMsgs.get(msg.get("msgsvrid")):
        #     logger.warning(f"[wx_hook] repeat msg filtered, msgsvrid={msg.get('msgsvrid')}")
        #     logger.debug(f"[wx_hook] repeat msg filtered, msg={msg}")
        #     return self.SUCCESS_MSG
        # channel.receivedMsgs[msg.get("msgsvrid")] = True

        wa_hook_msg = WaHookMessage(data, channel)

        logger.debug("[wx_hook] wa_hook_msg message: {}".format(wa_hook_msg))

        context = channel._compose_context(wa_hook_msg.ctype, wa_hook_msg.content, isgroup=wa_hook_msg.is_group,
                                           msg=wa_hook_msg)

        if context is None:
            return self.FAILED_MSG

        if check_allow_or_block_list(context, wainfo) is False:
            logger.debug(f"[wx_hook] check_allow_or_block_list failed")
            return self.FAILED_MSG

        # 增加需要的context
        context['wa_hook_msg'] = wa_hook_msg

        if wa_hook_msg.ctype == ContextType.TEXT:
            context['cmd_msgsvrid'] = self.cmd_msg_svrid.pop(0) if self.cmd_msg_svrid else wa_hook_msg.msg_id

        if wainfo and wainfo['api_base']:
            context['open_ai_api_base'] = wainfo['api_base']
            context['open_ai_api_key'] = wainfo['api_key']
            context['organization_id'] = wainfo['organization_id']

        if context:
            logger.debug(f"[wx_hook] context session_id is {context['session_id']}")
            channel.produce(context)

        return "success"


def check_allow_or_block_list(context, wxinfo):
    block_list = wxinfo.get('block_list')
    if block_list is None:
        block_list = '[]'
    block_list = json.loads(block_list)

    allow_list = wxinfo.get('allow_list')
    if allow_list is None:
        allow_list = '[]'
    allow_list = json.loads(allow_list)
    # 是否禁用所有群
    if context['isgroup']:
        group_block_list = wxinfo.get('group_block_list')
        if group_block_list is None:
            group_block_list = '[]'
        group_block_list = json.loads(group_block_list)
        if group_block_list and ("ALL" in group_block_list or context['receiver'] in group_block_list):
            logger.debug(
                f"[CHATGPT] --------------------已禁用改群或所有群-----------------")
            return False
    # 是否禁用所有用户
    elif block_list and ("ALL" in block_list or context['session_id'] in block_list):
        logger.debug(
            f"[CHATGPT] --------------------已禁用当前用户或所有用户-----------------")
        return False
    # 当没有允许所有群时
    if context['isgroup']:
        group_allow_list = wxinfo.get('group_allow_list')
        if group_allow_list is None:
            group_allow_list = '[]'
        group_allow_list = json.loads(group_allow_list)
        if group_allow_list and len(group_allow_list) > 0:
            # 是否允许当前群
            if "ALL" not in group_allow_list and context['receiver'] not in group_allow_list:
                logger.debug(
                    f"[CHATGPT] --------------------群不在白名单-----------------")
                return False
    # 当没有允许所有用户时
    elif allow_list and len(allow_list) > 0:
        # 是否允许当前用户
        if "ALL" not in allow_list and context['session_id'] not in allow_list:
            logger.debug(
                f"[CHATGPT] --------------------用户不在白名单-----------------")
            return False

    return True
