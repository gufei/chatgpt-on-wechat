import binascii
from tempfile import TemporaryFile, NamedTemporaryFile

import openai
import pilk

from bridge.context import ContextType
from channel.chat_message import ChatMessage
from common.log import logger
from config import conf
from xml.etree import ElementTree as ET


class WxHookMessage(ChatMessage):
    def __init__(self, msg, channel, selfwxid, private_ip, port):
        super().__init__(msg)

        logger.debug(f"[wx_hook] msg is {msg}")


        self.msg_id = msg.get("msgsvrid")
        self.create_time = msg.get("time")

        self.is_group = False
        if "fromtype" in msg and msg.get("fromtype") == "2":
            self.is_group = True
        elif "fromid" in msg and "@chatroom" in msg.get("fromid"):
            self.is_group = True


        if self.is_group and "@chatroom" in msg.get("fromid") and "fromgin" not in msg:
            msg["fromgid"] = msg.get("fromid")
            # msg["fromid"] = msg.get("toid")
            # msg["toid"] = msg.get("fromgid")

        if self.is_group and msg.get("fromtype") != "2":
            msg["fromtype"] = "2"

        if msg.get("msgtype") == "1":
            self.ctype = ContextType.TEXT
            self.content = msg.get("msg")
        elif msg.get("msgtype") == "34":
            self.ctype = ContextType.VOICE
            if self.is_group:
                msgsvrid = msg.get("msgsvrid")

                msgroot = ET.fromstring(msg.get("msg"))
                voicemsg = msgroot.find('voicemsg')
                length = voicemsg.get('length')
                clientmsgid = voicemsg.get('clientmsgid')

                voiceinfo = channel.getVoice(clientmsgid, length, msg.get("fromgid"), msgsvrid, private_ip, port)
                voice_hex = voiceinfo.get("voice_data_hex")
            else:
                voice_hex = msg.get("voice_hex")

            voice = binascii.unhexlify(voice_hex)
            temp = NamedTemporaryFile(dir="/tmp", prefix="silk_", suffix=".silk", delete=False)
            temp.write(voice)
            temp.seek(0)
            # wavTemp = NamedTemporaryFile(dir="/tmp", prefix="wav_", delete=False)
            # pilk.silk_to_wav(temp.name, wavTemp.name)
            self.content = temp.name
        else:
            raise NotImplementedError("Unsupported message type: {}".format(msg.get("msgtype")))

        if self.is_group:
            self.from_user_id = msg.get("toid")
            self.from_user_nickname = channel.getNickName(msg.get("toid"), private_ip, port)
            self.to_user_id = msg.get("fromid")
            self.to_user_nickname = channel.getNickName(msg.get("fromid"), private_ip, port)
        else:
            self.from_user_id = msg.get("fromid")
            self.from_user_nickname = channel.getNickName(msg.get("fromid"), private_ip, port)
            self.to_user_id = msg.get("toid")
            self.to_user_nickname = channel.getNickName(msg.get("toid"), private_ip, port)

        self.actual_user_id = self.from_user_id


        logger.debug(f"[wx_hook] actual_user_nickname is {self.from_user_nickname}")
        self.actual_user_nickname = self.from_user_nickname

        if self.is_group:
            if "fromgid" in msg:
                group = channel.getGroup(msg.get("fromgid"), private_ip, port)
                self.other_user_id = msg.get("fromgid")
                self.other_user_nickname = group.get("gname")
                self.group_id = msg.get("fromgid")
                self.group_name = group.get("gname")
            else:
                group = channel.getGroup(msg.get("fromid"), private_ip, port)
                self.other_user_id = msg.get("fromid")
                self.other_user_nickname = group.get("gname")
                self.group_id = msg.get("fromid")
                self.group_name = group.get("gname")
        else:
            if self.from_user_id != selfwxid:
                self.other_user_id = self.from_user_id
                self.other_user_nickname = self.from_user_nickname
            else:
                self.other_user_id = self.to_user_id
                self.other_user_nickname = self.to_user_nickname

        msgsource = msg.get("msgsource")
        self.is_at = False

        selfnickName = channel.getNickName(selfwxid, private_ip, port)
        logger.debug(f"[wx_hook] selfnickName is {selfnickName} selfwxid is {selfwxid}")

        if selfnickName != "" and "@" + selfnickName in self.content:
            self.is_at = True
        elif msgsource:
            # 解析xml格式，获取 atuserlist 判断是否有自己 selfwxid
            xmlstr = msgsource.replace('\\n', '').replace('\\t', '')
            logger.debug(f"[wx_hook] xmlstr is {xmlstr}")
            from xml.etree import ElementTree
            root = ElementTree.fromstring(xmlstr)
            atuserlist = root.find("./atuserlist")
            if atuserlist is not None:
                logger.debug(f"[wx_hook] atuserlist is {atuserlist.text}")
                for atuser in atuserlist.text.split(","):
                    if atuser == "":
                        continue
                    logger.debug(f"[wx_hook] atuser is {atuser}")
                    if atuser == selfwxid:
                        self.is_at = True
            else:
                logger.debug(f"[wx_hook] atuserlist is None")
