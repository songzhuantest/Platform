# cloudy about device
from flask import request
from flask_login import login_required

from app.blueprint.device import device
from app.libs.request_to import request_to, request_form
from app.models.device.device import Device

device_sq = Device()


@device.route('/yun/list', methods=['GET', 'POST'])
@login_required
def lists():
    return device_sq.yun_list()


@device.route('/yun/start', methods=['GET', 'POST'])
@login_required
def start():
    if request.method == 'POST':
        request_to(request).to_get_data()
        return device_sq.yun_connect(request_form.data)


@device.route('/yun/remove', methods=['GET', 'POST'])
@login_required
def remove():
    if request.method == 'POST':
        request_to(request).to_get_data()
        return device_sq.yun_remove(request_form.data)


@device.route('/yun/apk/install', methods=['GET','POST'])
@login_required
def install():
    if request.method == 'POST':
        request_to(request).to_get_data()
        return device_sq.yun_install(request_form.data)


@device.route('/yun/log', methods=['GET','POST'])
@login_required
def log():
    if request.method == 'POST':
        request_to(request).to_get_data()
        return device_sq.yun_log(request_form.data)






