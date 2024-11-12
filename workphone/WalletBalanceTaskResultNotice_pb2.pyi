from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WalletBankCardMessage(_message.Message):
    __slots__ = ("CardType", "BankName", "CardTail", "Desc")
    CARDTYPE_FIELD_NUMBER: _ClassVar[int]
    BANKNAME_FIELD_NUMBER: _ClassVar[int]
    CARDTAIL_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    CardType: int
    BankName: str
    CardTail: str
    Desc: str
    def __init__(self, CardType: _Optional[int] = ..., BankName: _Optional[str] = ..., CardTail: _Optional[str] = ..., Desc: _Optional[str] = ...) -> None: ...

class WalletBalanceTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Balance", "TrueName", "BankCard")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    TRUENAME_FIELD_NUMBER: _ClassVar[int]
    BANKCARD_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Balance: int
    TrueName: str
    BankCard: _containers.RepeatedCompositeFieldContainer[WalletBankCardMessage]
    def __init__(self, WeChatId: _Optional[str] = ..., Balance: _Optional[int] = ..., TrueName: _Optional[str] = ..., BankCard: _Optional[_Iterable[_Union[WalletBankCardMessage, _Mapping]]] = ...) -> None: ...
