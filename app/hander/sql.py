# 处理sql筛选
from sqlalchemy import or_, ColumnElement

from app.models import base


# class sqlhandler:
#     def __init__(self):
#         self.status = False
#         self.content = []
#         self.re = ()
#
#     def sql_select(self, data, table):
#         new = {}
#         for key, value in data.items():
#             if value:
#                 self.status = True
#                 new.update({key: value})
#         for key, value in new.items():
#             if type(value) is list:
#                 self.content.append(or_(getattr(table, key).in_(value))),
#             if type(value) is str:
#                 self.content.append(or_(getattr(table, key) == value)),

