# encoding:utf-8
import argparse
import base64
import os
import signal
import sys
import time
sys.path.append(os.getcwd()+'/workphone')

from flask import Flask
from channel import channel_factory
from channel.wechat.wxhook_channel import wx_hook_request, wx_hook_admin_request
from common import const
from config import load_config
from db.DBStorage import DBStorage
from plugins import *
import threading

from lib.itchat import *

from PIL import Image


def sigterm_handler_wrap(_signo):
    old_handler = signal.getsignal(_signo)

    def func(_signo, _stack_frame):
        logger.info("signal {} received, exiting...".format(_signo))
        conf().save_user_datas()
        if callable(old_handler):  # check old_handler
            return old_handler(_signo, _stack_frame)
        sys.exit(0)
        os.exit()

    signal.signal(_signo, func)


def start_channel(channel_name: str):
    channel = channel_factory.create_channel(channel_name)
    if channel_name in ["wx", "wxy", "wx_hook",'workphone', "whatsapp", "terminal", "wechatmp", "wechatmp_service", "wechatcom_app", "wework",
                        const.FEISHU, const.DINGTALK]:
        PluginManager().load_plugins()

    if conf().get("use_linkai"):
        try:
            from common import linkai_client
            threading.Thread(target=linkai_client.start, args=(channel,)).start()
        except Exception as e:
            pass
    channel.startup()


db_storage = DBStorage()
redis_conn = db_storage.get_redis_conn()


def run(app: Flask):
    try:
        # load config
        load_config()
        # ctrl + c
        sigterm_handler_wrap(signal.SIGINT)
        # kill signal
        sigterm_handler_wrap(signal.SIGTERM)

        # create channel
        channel_name = conf().get("channel_type", "wx")

        # if channel_name == "wx" or channel_name == "wx_hook":
        #     threading.Thread(target=app.run, args=("0.0.0.0", 5000), daemon=True).start()

        if "--cmd" in sys.argv:
            channel_name = "terminal"

        if channel_name == "wxy":
            os.environ["WECHATY_LOG"] = "warn"

        start_channel(channel_name)

        while True:
            time.sleep(1)
    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)


app = Flask(__name__)


@app.route('/checkStatus')
def checkStatus():
    if conf().get("channel_type") != "wx_hook":
        return "当前不是微信HOOK模式"

    status = wx_hook_request("IsLoginStatus", {})
    logger.info(f"[wx_hook] check status: {status}")

    if status is None:
        # wx_hook_port int转字符串
        protStatus = wx_hook_admin_request("Get_PortOccupiedInfo", {"CheckPort": conf().get("wx_hook_port")})
        if protStatus.get("Occupied") == "0":
            wx_hook_admin_request("StartWechat", {"StartPort": conf().get("wx_hook_port")})
            return "<head><meta http-equiv='refresh' content='5'></head>正在启动微信，请过5秒后再次刷新页面......" + "<div><input type='button' onclick='javascript:location.reload();' value='刷新当前页面'></div>"
        else:
            return "<head><meta http-equiv='refresh' content='5'>获取微信状态失败，请5秒后再次刷新页面......" + "<div><input type='button' onclick='javascript:location.reload();' value='刷新当前页面'></div>"

    # 请扫码登陆
    if status.get("onlinestatus") == "0":
        qrcode = wx_hook_request("GetLoginQRCode", {})
        return "<img src='" + qrcode.get(
            "base64") + "' width='300px' height='300px'><p><div>扫码登陆完成后3秒刷新本页面~</div>" + "<div><input type='button' onclick='javascript:location.reload();' value='刷新当前页面'></div>"

    # 需在手机上完成操作
    if status.get("onlinestatus") == "1":
        return status.get("msg")

    if status.get("onlinestatus") == "2":
        return status.get("msg") + " 当前登陆进度：" + status.get(
            "login_loading") + "<div><input type='button' onclick='javascript:location.reload();' value='刷新当前页面'></div>"

    # 已登陆状态
    if status.get("onlinestatus") == "3":
        return status.get("msg") + " 当前登陆用户：" + status.get(
            "nickname") + "<div><input type='button' onclick='javascript:location.reload();' value='刷新当前页面'></div>"

    # 正在退出微信
    if status.get("onlinestatus") == "4":
        return status.get("msg")

    # 让点击登陆，这时刷新二维码，仍使用二维码登陆
    if status.get("onlinestatus") == "5":
        wx_hook_request("RefreshLoginQRCode", {})
        qrcode = wx_hook_request("GetLoginQRCode", {})
        return "<img src='" + qrcode.get(
            "base64") + "' width='300px' height='300px'><p><div>扫码登陆完成后3秒刷新本页面~</div>" + "<div><input type='button' onclick='javascript:location.reload();' value='刷新当前页面'></div>"


@app.route('/wxlogin')
async def wxlogin():
    if conf().get("channel_type") != "wx":
        if conf().get("channel_type") == "wx_hook":
            return "已经启用新的登陆页，请使用 <a href=\"/checkStatus\">检查状态</a> 进行登陆"
        else:
            return "当前不是微信登陆模式"

    logger.info("当前是否正在进行登陆？ %s", str(instance.isLogging))

    if instance.isLogging == False and instance.loginInfo.get("User") != None:
        return "已经登陆,当前登陆账号是：" + instance.loginInfo.get("User").NickName
    else:
        imgByte = get_QR()
        # io.BytesIO() 转成 base64
        imgBase = "data:image/png;base64," + str(base64.b64encode(imgByte.getvalue()), 'utf-8')
        return "<img src='" + imgBase + "'>" + "<br>" + "请扫描二维码登陆"


if __name__ == "__main__":
    run(app)
    # parser = argparse.ArgumentParser(description='消息中间处理程序')
    # parser.add_argument('-c', '--config', help='设置配置文件，默认值是 ./config.json')
    # args = parser.parse_args()
    #
    # if args.config:
    #     configfile = args.config
    # else:
    #     configfile = "./config.json"
    #
    # if args.help:
    #     parser.print_help()
    # else:
    #     run(app)
