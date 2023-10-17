# monkey model

from sqlalchemy import Column, Integer, String, Enum, desc

from app import db
from app.models import Base
from app.view_model.monkey.monkey import MonkeyMessage, MonkeyCollection

MM = MonkeyMessage()
MC = MonkeyCollection()


class Monkey_form(Base):
    __monkey__ = 'monkey_form'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device = Column(String(50), nullable=False)
    version = Column(String(20), nullable=True)
    branch = Column(Integer, nullable=False)
    events = Column(Integer, nullable=False)
    model = Column(Enum('0', '1'), nullable=False)
    package = Column(String(1000), nullable=False)
    type = Column(Integer, nullable=False, default=7)
    status = Column(Integer, default=0)  # 0 未开始 1 执行中 2 执行结束

    @staticmethod
    def submit_form(condition: {}):
        form = Monkey_form()
        form.device = condition.get('ip')
        form.events = condition.get('number')
        form.branch = condition.get('count')
        form.model = condition.get('model')
        form.version = condition.get('version')
        form.package = str(condition.get('package')['value'])

        try:
            db.session.add(form)
            db.session.commit()
            MM.success('添加工单成功')
        except Exception as e:
            print(e)
            MM.fail('添加工单失败')
        return MM.message

    @staticmethod
    def form_list(condition: {}):
        form = Monkey_form()
        monkey_list = form.query.order_by(desc(Monkey_form.create_time)).all()
        MC.fill(monkey_list)
        return MC.to_dic()


