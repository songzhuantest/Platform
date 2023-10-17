from app.libs import enums


class DeviceModel:
    def __init__(self, data):
        self.id = data.id
        self.sn = data.sn
        self.type = data.type
        self.use = data.use
        self.storage = data.storage
        self.owner = data.owner
        self.description = data.description
        self.address = data.address
        self.stage = data.stage
        self.remote = data.remote
        self.ip = data.ip

    def to_dic(self):
        dic = dict()
        dic['id'] = self.id
        dic['sn'] = self.sn
        dic['type'] = self.type
        dic['use'] = self.use
        dic['storage'] = self.storage
        dic['owner'] = self.owner
        dic['description'] = self.description
        dic['address'] = self.address
        dic['stage'] = self.stage
        dic['remote'] = self.remote
        dic['ip'] = self.ip
        return dic


class DeviceCollection:
    def __init__(self):
        self.total = 0
        self.data = []

    def fill(self, device_list):
        self.total = len(device_list)
        self.data = [DeviceModel(device).to_dic() for device in device_list]

    def to_dic(self):
        dic = dict()
        dic['total'] = self.total
        dic['data'] = self.data
        return dic


class DeviceMessage:
    def __init__(self):
        self.message = {}

    def fail(self, data):
        self.message = {'code': enums.CodeStatus.Fail.value, 'message': data if data else '请求失败'}

    def success(self, data=None, **kwargs):
        self.message = {'code': enums.CodeStatus.Success.value, 'message': data if data else '请求成功'}
        self.message.update(kwargs)



