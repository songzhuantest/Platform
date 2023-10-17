#
import json

from multidict import MultiDict


class request_form:
    def __init__(self):
        self.data = {}


class request_to:
    def __init__(self, content):
        self.content = content

    def to_get_data(self):
        request_form.data = json.loads(self.content.get_data().decode('utf-8'))

    @staticmethod
    def to_multidict(data):
        req = MultiDict()
        for key, value in data.items():
            req.add(key, value)
        return req
