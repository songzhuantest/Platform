from flask import request

from . import monkey
from ...libs.request_to import request_to, request_form
from ...models.monkey.monkey import Monkey_form

MK = Monkey_form()


@monkey.route('/form', methods=['POST', 'GET'])
def monkey_form():
    pass


@monkey.route('/form/add', methods=['POST', 'GET'])
def monkey_form_add():
    if request.method == 'POST':
        request_to(request).to_get_data()
        re = MK.submit_form(request_form.data)
        print(re)
        return re


@monkey.route('/form/list', methods=['POST', 'GET'])
def monkey_form_list():
    if request.method == 'POST':
        request_to(request).to_get_data()
        re = MK.form_list(request_form.data)
        print(re)
        return re


@monkey.route('/exec', methods=['POST', 'GET'])
def monkey_exec():
    if request.method == 'POST':
        request_to(request).to_get_data()
        re = MK.form_list(request_form.data)
        print(re)
        return re
