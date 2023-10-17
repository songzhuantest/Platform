# 注册
from app.libs import enums


class LoginModel:
    def __init__(self):
        self.message = {}

    def login_success(self, data=None):
        self.message = {'code': enums.CodeStatus.Success.value, 'message': data if data else '登录成功'}

    def login_fail(self, data=None):
        self.message = {'code': enums.CodeStatus.Fail.value, 'message': data if data else '登录失败'}

    def password_fail(self, data=None):
        self.message = {'code': enums.CodeStatus.Fail.value, 'message': data if data else '密码不正确'}

    def logout_success(self, data=None):
        self.message = {'code': enums.CodeStatus.Success.value, 'message': data if data else '退出成功'}


class LoginInfo:
    def __init__(self, user):
        self.id = user.id
        self.nickname = user.nickname
        self.role = user.role.value

    def to_dic(self):
        dic = dict()
        dic['id'] = self.id
        dic['nickname'] = self.nickname
        dic['role'] = self.role
        return dic
