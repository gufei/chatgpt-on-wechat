"""
channel factory
"""
from common import const
from .channel import Channel


def create_channel(channel_type) -> Channel:
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    ch = Channel()
    if channel_type == "wx":
        from channel.wechat.wechat_channel import WechatChannel
        ch = WechatChannel()
    elif channel_type == "wxy":
        from channel.wechat.wechaty_channel import WechatyChannel
        ch = WechatyChannel()
    elif channel_type == "wx_hook":
        from channel.wechat.wxhook_channel import WxHookChannel
        ch = WxHookChannel()
    elif channel_type == "workphone":
        from channel.wechat.workphone_channel import WorkPhoneChannel
        ch = WorkPhoneChannel()
    elif channel_type == "workphone_wecom":
        from channel.wework.workphone_channel import WorkPhoneChannel
        ch = WorkPhoneChannel()
    elif channel_type == "whatsapp":
        from channel.whatsapp.whatsapp_channel import WaHookChannel
        ch = WaHookChannel()
    elif channel_type == "terminal":
        from channel.terminal.terminal_channel import TerminalChannel
        ch = TerminalChannel()
    elif channel_type == "wechatmp":
        from channel.wechatmp.wechatmp_channel import WechatMPChannel
        ch = WechatMPChannel(passive_reply=True)
    elif channel_type == "wechatmp_service":
        from channel.wechatmp.wechatmp_channel import WechatMPChannel
        ch = WechatMPChannel(passive_reply=False)
    elif channel_type == "wechatcom_app":
        from channel.wechatcom.wechatcomapp_channel import WechatComAppChannel
        ch = WechatComAppChannel()
    elif channel_type == "wework":
        from channel.wework.wework_channel import WeworkChannel
        ch = WeworkChannel()
    elif channel_type == const.FEISHU:
        from channel.feishu.feishu_channel import FeiShuChanel
        ch = FeiShuChanel()
    elif channel_type == const.DINGTALK:
        from channel.dingtalk.dingtalk_channel import DingTalkChanel
        ch = DingTalkChanel()
    elif channel_type == "wework_hook":
        from channel.wework.weworkhook_channel import WeworkHookChannel
        ch = WeworkHookChannel()
    else:
        raise RuntimeError
    ch.channel_type = channel_type
    return ch
