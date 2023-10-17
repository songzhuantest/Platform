

class ToolModel:
    def __init__(self, data):
        self.active = data.active
        self.created_at = data.created_at
        self.created_by = data.created_by
        self.description = data.description
        self.id = data.id
        self.plan_id = data.plan_id
        self.project_id = data.project_id
        self.title = data.title

    def to_dic(self):
        dic = dict()
        dic['id'] = self.id
        dic['plan_id'] = self.plan_id
        dic['project_id'] = self.project_id
        dic['title'] = self.title
        dic['description'] = self.description
        dic['created_at'] = self.created_at
        dic['created_by'] = self.created_by
        dic['active'] = self.active
        return dic


class ToolCollection:
    def __init__(self):
        self.total = 0
        self.data = []

    def fill(self, tool_list):
        self.total = len(tool_list)
        self.data = [ToolModel(tool).to_dic() for tool in tool_list]

    def to_dic(self):
        dic = dict()
        dic['total'] = self.total
        dic['data'] = self.data
        return dic
