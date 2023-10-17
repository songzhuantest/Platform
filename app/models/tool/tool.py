from sqlalchemy import Column, Integer, String

from app.models import Base

from app.view_model.tool.tool import ToolCollection

tool_c = ToolCollection()


class Tool(Base):
    __tablename__ = 'tool'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, nullable=False)
    plan_id = Column(String(200), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False)
    created_by = Column(String(50), nullable=False)
    created_at = Column(String(80), nullable=False)

    @staticmethod
    def list():
        tool_list = Tool.query.filter().all()
        tool_c.fill(tool_list)
        return tool_c.to_dic()
