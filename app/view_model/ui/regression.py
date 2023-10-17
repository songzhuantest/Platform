# 封装样式
import time

class report:
    def __init__(self, data):
        self.id = data.id
        self.date = data.date
        self.version = data.version
        self.group = data.group
        self.device = data.device
        self.report = data.report

    def to_dict(self):
        dic = dict()
        dic['id'] = self.id
        dic['date'] = self.date.strftime("%Y-%m-%d")
        dic['version'] = self.version
        dic['group'] = self.group
        dic['device'] = self.device
        dic['report'] = self.report
        return dic


class ReportCollection:
    def __init__(self):
        self.lists = []

    def fill(self, report_list):
        self.lists = [report(report_one).to_dict() for report_one in report_list]
