# encoding:utf-8

from enum import Enum


class ReplyType(Enum):
    TEXT = 1  # 文本
    VOICE = 2  # 音频文件
    IMAGE = 3  # 图片文件
    IMAGE_URL = 4  # 图片URL
    VIDEO_URL = 5  # 视频URL
    FILE = 6  # 文件
    CARD = 7  # 微信名片，仅支持ntchat
    INVITE_ROOM = 8  # 邀请好友进群
    INFO = 9
    ERROR = 10
    TEXT_ = 11  # 强制文本
    VIDEO = 12
    MINIAPP = 13  # 小程序
    JSON_MULTIPLE_RESP = 14  # JSON多条回复数据
    ShiPinHao = 24  # 视频号
    LOCATION = 48 # 位置消息


    def __str__(self):
        return self.name


class Reply:
    def __init__(self, type: ReplyType = None, content=None, receiver=None):
        self.type = type
        self.content = content
        self.receiver = receiver


    def __str__(self):
        return "Reply(type={}, content={}, receiver={})".format(self.type, self.content, self.receiver)
