from flask import request
from flask_login import login_required

from app.blueprint.tool import tool
from app.libs.request_to import request_to, request_form
from app.models.tool.tool import Tool

tool_sq = Tool()


@tool.route('/list', methods=['GET', 'POST'])
@login_required
def tool_list():
    if request.method == 'POST':
        return tool_sq.list()