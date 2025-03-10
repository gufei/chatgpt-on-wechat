import json
import time
import requests
import web
import hashlib
from Crypto.Cipher import AES
import base64
import uuid


from bridge.context import Context, ContextType
from channel.chat_channel import ChatChannel
from channel.wework.weworkhook_message import WeworkHookMessage
from common.expired_dict import ExpiredDict
from common.log import logger
from config import conf
from bridge.reply import Reply, ReplyType
from lib.file_tool import is_image_file


class WeworkHookChannel(ChatChannel):
    NOT_SUPPORT_REPLYTYPE = [ReplyType.VOICE, ReplyType.FILE]

    token = ''
    token_expire = 0

    def __init__(self):
        super().__init__()
        # 历史消息id暂存，用于幂等控制
        self.receivedMsgs = ExpiredDict(60 * 60 * 7.1)


    # 从API里获取指定的客户信息
    def get_xunji_contact(self, robot_id: str, account_id: str):
        # http://106.55.11.68:9898/md/01-%E6%9C%BA%E5%99%A8%E4%BA%BA%E7%9B%B8%E5%85%B3/04-%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%AE%A2%E6%88%B7/1406-GetRobotAccountByIdsV2.html
        url = "https://api.xunjinet.com.cn/gateway/qopen/GetRobotAccountByIdsV2"
        data = {
            "robot_id": robot_id,
            "account_id_list": [account_id],
            "external_user_id_list": [],
            "need_tag_info": False,
            "need_user_attr_field": False,
            "need_user_attr_sys_field": False,
            "need_empty_attr_field": False,
        }
        headers = {
            "Content-Type": "application/json",
            "Token": self.get_access_token(),
        }
        res = requests.post(url, headers=headers, json=data, timeout=(5, 10))
        logger.debug(f"[wework_hook] get contact, url: {url} data: {data} res: {res.json(strict=False)}")
        json_data = res.json(strict=False)
        if json_data.get('errcode') != 0:
            logger.error(f"get contact failed:{json_data}")
        else:
            if len(json_data.get('data').get('account_list')) > 0:
                logger.info(f"get contact success:{json_data}")
                for account in json_data.get('data').get('account_list'):
                    return {
                        "robot_id": robot_id,
                        "account_id": account_id,
                        "nickname": account.get('profile').get('name'),
                        "avatar": account.get('profile').get('avatar'),
                    }

            return None

    # 获取昵称（先从db里查，如果没有再通过API获取，并写入DB里）
    def getNickName(self, robot_id: str, account_id: str):
        wxinfo = self.get_xunji_contact(robot_id, account_id)

        if wxinfo is None:
            return ''
        else:
            return wxinfo.get('nickname')

    # 获取访问token
    def get_access_token(self):
        # @see http://106.55.11.68:9898/md/__01-start.html
        app_key = conf().get('wework_app_key')
        app_secret = conf().get('wework_app_secret')

        if self.token != "" and self.token_expire > int(time.time()):
            return self.token
        else:
            url = "https://api.xunjinet.com.cn/gateway/qopen/GetAccessToken"
            data = {
                "app_key": app_key,
                "app_secret": app_secret
            }
            headers = {
                "Content-Type": "application/json",
            }
            res = requests.post(url, headers=headers, json=data, timeout=(5, 10))
            logger.debug(f"[wework_hook] get access_token, url: {url} data: {data} res: {res.json(strict=False)}")
            json_data = res.json(strict=False)
            # logger.info(f"json_data={json_data}")
            if json_data.get('errcode') == 0:
                self.token = json_data.get('data').get('data').get('access_token')
                self.token_expire = json_data.get('data').get('data').get('expires_in') + int(time.time())
                return self.token

            return ''


    # 发送回复消息
    def send_message(self, robot_id, account_id, content_type, content, href, title, desc):
        # @see http://106.55.11.68:9898/md/02-%E6%B6%88%E6%81%AF%E7%9B%B8%E5%85%B3/2002-SendMessageToAccount__1.html
        url = "https://api.xunjinet.com.cn/gateway/qopen/SendMessageToAccount"
        msg_id = str(uuid.uuid4())

        # 如果有错误信息，去掉内容里的[ERROR]\n
        if content.startswith('[ERROR]\n'):
            content = content[len('[ERROR]\n'):]

        data = {
            "robot_id": robot_id,
            "account_id": account_id,
            "msg_id": msg_id,
            "dead_line": int(time.time())+180,
            "msg_list": [
                {
                    "msg_num": 1,
                    "msg_type": content_type,
                    "msg_content": content,
                    "voice_time": 0,
                    "href": href,
                    "title": title,
                    "desc": desc
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Token": self.get_access_token(),
        }
        res = requests.post(url, headers=headers, json=data, timeout=(5, 10))
        logger.debug(f"[wework_hook] send reply message, url: {url} data: {data} res: {res.json(strict=False)}")
        json_data = res.json(strict=False)
        if json_data.get('errcode') != 0:
            logger.error(f"send reply message failed:{json_data}")
        else:
            logger.info(f"send reply message success:{json_data}")

    # 启动服务
    def startup(self):
        # 启动获取一次token，持续2小时有效
        self.get_access_token()

        # 启动回调监听
        urls = (
            '/localhook/wework/receiveChatBotMsg', 'channel.wework.weworkhook_channel.WeworkHookController'
        )
        app = web.application(urls, globals(), autoreload=False)
        port = conf().get("wework_hook_callback_port", 9030)
        web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", port))

    def send(self, reply: Reply, context: Context):

        logger.info(f"[wework_hook] in send_function reply={reply}")

        if reply.type == ReplyType.TEXT or reply.type == ReplyType.TEXT_:
            content_type = 1
            content = reply.content
        else:
            content = reply.content
            content_type = reply.type
            if is_image_file(content):
                content_type = 3

        self.send_message(
            context['robot_id'],
            context['sender_id'],
            content_type,
            content,
            context['href'],
            context['title'],
            context['desc'],
        )


class WeworkHookController:
    wework_app_key = conf().get('wework_app_key')
    wework_token = conf().get('wework_token')
    wework_encoding_key = conf().get('wework_encoding_key')

    FAILED_MSG = 'error'
    SUCCESS_MSG = 'success'

    # 对字符串进行md5加密
    def calculate_md5(self, text: str):
        """計算字串的 MD5 值"""
        md5_hash = hashlib.md5()  # 建立md5物件
        md5_hash.update(text.encode('utf-8'))  # 更新md5物件 (encode將文字轉換為utf-8字節)
        return md5_hash.hexdigest()  # 返回16進制MD5值

    # 校验签名内容
    def check_signature(self, data: dict[str, str]):
        my_dict = {
            'app_key': self.wework_app_key,
            'token': self.wework_token,
            'nonce': data.get('nonce'),
            'timestamp': data.get('timestamp'),
            'encoding_content': data.get('encoding_content'),
        }
        sorted_values = sorted(my_dict.values())
        sort_str = ''.join(sorted_values)
        if self.calculate_md5(sort_str) == data.get('signature'):
            return True
        else:
            return False

    def strip_PKCS5_padding(self, data: bytes) -> bytes:
        pad_len = data[-1]
        if pad_len == 125:
            return data
        return data[:-pad_len]

    # AES解密
    def aes_decrypt(self, data: str, key: str) -> str:
        raw_data = base64.b64decode(data)

        # 获取 IV（与 PHP 相同，取 key 的前 16 字节）
        iv = key[:16].encode('utf-8')
        key_bytes = key.encode('utf-8')

        # ZERO_PADDING 实现方式：解密前不做 unpad 处理，手动去除补位
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(raw_data)

        # 去除换行符
        decrypted_data = decrypted_data.replace(b'\n', b'')

        # 去除 PKCS5Padding
        result = self.strip_PKCS5_padding(decrypted_data)

        return result.decode('utf-8', errors='ignore')

    # 这里要改成根据 app_key 和 token 去获取当前这人的 encoding_key
    def get_encoding_key(self, app_key: str, token: str):
        if app_key is None or token is None:
            return None

        from app import db_storage
        xunji_token = db_storage.get_xunji_token(app_key, token)
        return xunji_token

    def POST(self):
        rawdata = json.loads(web.data().decode("utf-8"), strict=False)
        logger.info(f"[wework_hook] receive request: {rawdata}")

        # 对接收的内容验证签名，保证安全性
        if not self.check_signature(rawdata):
            return self.FAILED_MSG

        #
        # 这里改成根据信息去查询这个app_key对应的 encoding_key
        # 每个用户的app_key, app_secret, encoding_key 都不同
        # 这样每个人的信息都需要去做区分


        wxinfo = self.get_encoding_key(rawdata.get('app_key'), rawdata.get('token'))
        logger.debug(f"[wework_hook] app_key={rawdata.get('app_key')} token={rawdata.get('token')} wxinfo={wxinfo}")
        if wxinfo is None:
            return self.FAILED_MSG

        data_str = self.aes_decrypt(rawdata.get('encoding_content'), wxinfo.get('encoding_key'))
        data = json.loads(data_str)
        logger.info(f"[wework_hook] decrypt data: {data}")
        event_type = data.get('event_type')

        # 被动私聊消息（只处理消息回调）
        # 其他回调一律返回错误。 官方文档里只要内容里带：success 都算成功
        # @see http://106.55.11.68:9898/md/02-%E6%B6%88%E6%81%AF%E7%9B%B8%E5%85%B3/01-%E4%BA%8B%E4%BB%B6%E9%80%9A%E7%9F%A5/2101-GetPrivateMessageCallback.html
        if event_type != 40023 and event_type != 20002:
            return self.FAILED_MSG

        channel = WeworkHookChannel()
        channel.user_id = data.get("sender_id")

        # 过滤自己的消息
        selfwxid = ''
        if data.get("sender_id") != "":
            selfwxid = data.get("sender_id")

        if selfwxid == "":
            logger.debug(f"[wx_hook] selfwxid is empty")
            return self.FAILED_MSG

        # 只处理文本+语音+图片+视频
        validTypes = (1, 2, 3, 4)
        if data.get("msg_type") not in validTypes:
            logger.debug(f"[wework_hook] not a valid wework message, msg_type={data.get('msg_type')}")
            return self.FAILED_MSG

        if channel.receivedMsgs.get(data.get("msg_id")):
            logger.warning(f"[wework_hook] repeat msg filtered, msg_id={data.get('msg_id')}")
            return self.SUCCESS_MSG

        channel.receivedMsgs[data.get("msg_id")] = True

        isgroup = event_type == 20002
        isat = event_type == 20002
        wework_hook_msg = WeworkHookMessage(data, channel, isgroup, isat)

        logger.debug("[wework_hook] wework_hook_msg message: {}".format(wework_hook_msg))

        context = channel._compose_context(wework_hook_msg.ctype, wework_hook_msg.content,
                                           isgroup=wework_hook_msg.is_group,
                                           msg=wework_hook_msg)

        if context is None:
            return self.FAILED_MSG

        # 增加需要的context
        context['channel_type'] = 'wework_hook'
        context['wework_hook_msg'] = wework_hook_msg
        context['wxid'] = data.get('robot_id')
        context['receiver'] = data.get('receiver_id')
        context['robot_id'] = data.get('robot_id')
        context['sender_id'] = data.get('sender_id')
        context['msg_type'] = data.get('msg_type')
        context['voice_time'] = data.get('voice_time')
        context['href'] = data.get('href', '')
        context['title'] = data.get('title', '')
        context['desc'] = data.get('desc', '')
        context['open_ai_api_base'] = wxinfo.get('api_base')
        context['open_ai_api_key'] = wxinfo.get('api_key')
        context['content'] = wework_hook_msg.content

        # logger.debug(f"[wework_hook] context is {context}")
        if context:
            logger.debug(f"[wework_hook] context session_id is {context['session_id']}")
            channel.produce(context)

        return self.SUCCESS_MSG
