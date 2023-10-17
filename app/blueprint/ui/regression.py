# regression
from flask import request
from flask_login import login_required

from app.blueprint.ui import ui
from app.libs.request_to import request_to, request_form
from app.models.ui.regression.regression import Regression
from app.view_model.ui.regression import ReportCollection

Reg_sq = Regression()


@ui.route('/regression/report', methods=['GET', 'POST'])
# @login_required
def report():
    if request.method == 'POST':
        return Reg_sq.reports()


@ui.route('regression/add', methods=['GET', 'POST'])
# @login_required
def enter():
    if request.method == 'POST':
        request_to(request).to_get_data()
        print(request_form.data)
        return Reg_sq.add(request_form.data)
