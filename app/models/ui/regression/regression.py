from flask_sqlalchemy import query
from sqlalchemy import Column, Integer, String, Date, Enum

from app import db
from app.libs.enums import CodeStatus, MessageContent
from app.libs.result import to_return
from app.models import Base
from app.view_model.ui.regression import ReportCollection
from datetime import datetime
from sqlalchemy import desc

Report_Co = ReportCollection()


class Regression(Base):
    __tablename__ = 'ui_regression'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date(), nullable=False)
    version = Column(String(200), nullable=False)
    group = Column(Enum('全部用例', '其他用例', '专项用例'), nullable=False)
    device = Column(Enum('Pad-12.7寸', 'Pad-13.7寸'), nullable=False)
    report = Column(String(200), nullable=False)

    @staticmethod
    def reports():
        reg = Regression()
        report_list = reg.query.order_by(desc(Regression.date)).all()
        Report_Co.fill(report_list)
        # print(Report_Co.lists)
        dic = {}
        dic.update({'reg': Report_Co.lists})
        print(dic)
        return to_return(data=dic)

    @staticmethod
    def add(data: dict = {}):
        if data:
            reg = Regression()
            print(datetime.strptime(data.get('date'), "%Y-%m-%d"))
            reg.date = data.get('date')
            reg.version = data.get('version')
            reg.group = data.get('group')
            reg.device = data.get('device')
            reg.report = data.get('report')

            try:
                db.session.add(reg)
                db.session.commit()
                to_return(CodeStatus.Success)
                print(to_return())
                print('12')
            except Exception as e:
                print('qwe')
                print(e)
                to_return(CodeStatus.Fail, data={'message': str(e)}, message=MessageContent.Fail)
        else:
            pass
        return to_return()

