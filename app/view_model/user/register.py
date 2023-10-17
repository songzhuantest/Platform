# 注册
from app.libs import enums


class RegisterModel:
    def __init__(self):
        self.message = {}

    def send_success(self, data=None):
        self.message = {'code': enums.CodeStatus.Success.value, 'message': data if data else '验证码发送成功'}

    def send_fail(self, data=None):
        self.message = {'code': enums.CodeStatus.Fail.value, 'message': data if data else '验证码发送失败'}

    def sms_fail(self, data=None):
        self.message = {'code': enums.CodeStatus.Fail.value, 'message': data if data else 'validate auth fail'}

    def register_success(self, data=None):
        self.message = {'code': enums.CodeStatus.Success.value, 'message': data if data else '恭喜你，注册成功'}

    def register_fail(self, data=None):
        self.message = {'code': enums.CodeStatus.Success.value, 'message': data if data else '注册失败，请重试'}


    # @staticmethod
    # def sms_check(self,data):
    #     from app.manage import app
    #                 app.config['']

