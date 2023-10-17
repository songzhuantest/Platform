

# user
from enum import Enum


class RoleStatus(Enum):
    admin = 1
    tester = 2
    developer = 3
    other = 4


class CodeStatus(Enum):
    Success = '200'
    Fail = '500'
    unauthorized = '401'
    HttpError = '419'


class MessageContent():
    Success = '成功'
    Fail = '失败'


# device


class DeviceStatus(Enum):
    using = 1
    stopped = 2


class DeviceRemote(Enum):
    Remoting = 1
    TemporaryRemoting = 2
    Local = 0



