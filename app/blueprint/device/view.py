from flask import request
from flask_login import login_required, current_user

from . import device
from app.libs.request_to import request_to, request_form
from app.models.device.device import Device, add_device
# device = Device()
from ...view_model.device.device import DeviceCollection

device_sq = Device()
device_co = DeviceCollection()


@device.route('/list', methods=['GET', 'POST'])
@login_required
def device_list():
    if request.method == 'POST':
        from ...manage import app
        request_to(request).to_get_data()
        # 暂不做校验
        print(request_form.data)
        devices = device_sq.search_device(request_form.data)
        device_co.fill(devices)
        print(app.config['APK_UPLOAD_PATH'])
        return device_co.to_dic()


@device.route('/update', methods=['GET', 'POST'])
@login_required
def device_update():
    if request.method == 'POST':
        request_to(request).to_get_data()
        return device_sq.update_device(request_form.data)


@device.route('/add', methods=['GET', 'POST'])
@login_required
def device_add():
    if request.method == 'POST':
        request_to(request).to_get_data()
        return add_device(request_form.data)


@device.route('/delete', methods=['GET', 'POST'])
@login_required
def device_del():
    if request.method == 'POST':
        request_to(request).to_get_data()
        return device_sq.delete_device(request_form.data)



