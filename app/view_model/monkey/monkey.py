from app.libs import enums


class MonkeyMessage:
    def __init__(self):
        self.message = {}

    def fail(self, data):
        self.message = {'code': enums.CodeStatus.Fail.value, 'message': data if data else '请求失败'}

    def success(self, data=None, **kwargs):
        self.message = {'code': enums.CodeStatus.Success.value, 'message': data if data else '请求成功'}
        self.message.update(kwargs)


class MonkeyModel:
    def __init__(self, data):
        self.id = data.id
        self.device = data.device
        self.version = data.version
        self.branch = data.branch
        self.events = data.events
        self.model = data.model
        self.package = data.package
        self.type = data.type
        self.status = data.status
        self.consume = data.branch * data.events * 0.35
        # self.remote = data.remote
        # self.ip = data.ip

    def to_dic(self):
        dic = dict()
        dic['id'] = self.id
        dic['device'] = self.device
        dic['version'] = self.version
        dic['branch'] = self.branch
        dic['events'] = self.events
        dic['model'] = self.model
        dic['package'] = self.package
        dic['type'] = self.type
        dic['status'] = self.status
        dic['consume'] = self.consume
        # dic['ip'] = self.ip
        return dic


class MonkeyCollection:
    def __init__(self):
        self.total = 0
        self.data = []

    def fill(self, monkey_list):
        self.total = len(monkey_list)
        self.data = [MonkeyModel(monkey).to_dic() for monkey in monkey_list]

    def to_dic(self):
        dic = dict()
        dic['total'] = self.total
        dic['data'] = self.data
        return dic


