from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CDNFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NoteMsg_Picture: _ClassVar[CDNFileType]
    NoteMsg_Thumb: _ClassVar[CDNFileType]
    NoteMsg_Video: _ClassVar[CDNFileType]
    NoteMsg_File: _ClassVar[CDNFileType]
    ChatMsg_Picture: _ClassVar[CDNFileType]
    ChatMsg_Thumb: _ClassVar[CDNFileType]
    ChatMsg_Video: _ClassVar[CDNFileType]
    ChatMsg_File: _ClassVar[CDNFileType]
    ChatMsg_Emoji: _ClassVar[CDNFileType]
NoteMsg_Picture: CDNFileType
NoteMsg_Thumb: CDNFileType
NoteMsg_Video: CDNFileType
NoteMsg_File: CDNFileType
ChatMsg_Picture: CDNFileType
ChatMsg_Thumb: CDNFileType
ChatMsg_Video: CDNFileType
ChatMsg_File: CDNFileType
ChatMsg_Emoji: CDNFileType

class CDNDownloadFileTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "CdnUrl", "CdnKey", "FileType", "FileId", "FileFmt", "FileSize", "MsgSvrId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CDNURL_FIELD_NUMBER: _ClassVar[int]
    CDNKEY_FIELD_NUMBER: _ClassVar[int]
    FILETYPE_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    FILEFMT_FIELD_NUMBER: _ClassVar[int]
    FILESIZE_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    CdnUrl: str
    CdnKey: str
    FileType: CDNFileType
    FileId: str
    FileFmt: str
    FileSize: int
    MsgSvrId: int
    def __init__(self, WeChatId: _Optional[str] = ..., CdnUrl: _Optional[str] = ..., CdnKey: _Optional[str] = ..., FileType: _Optional[_Union[CDNFileType, str]] = ..., FileId: _Optional[str] = ..., FileFmt: _Optional[str] = ..., FileSize: _Optional[int] = ..., MsgSvrId: _Optional[int] = ...) -> None: ...
