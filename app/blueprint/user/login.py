# login 登录
from flask import request, render_template, url_for, redirect

from . import user
from app.forms.user.login import LoginForm
from app.libs.request_to import request_to, request_form
from ...models.user.user import User
from ...view_model.user.login import LoginModel, LoginInfo
from flask_login import login_user, logout_user, current_user
login_v = LoginModel()


@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        request_to(request).to_get_data()
        req = request_to.to_multidict(request_form.data)
        form = LoginForm(req)
        user = User.query.filter_by(_nickname=request_form.data.get('nickname')).first()
        if form.validate() and user:
            if user.is_same_password(request_form.data.get('password')):
                # user.generate_token()
                login_user(user, remember=True)
                login_v.login_success()
        else:
            login_v.login_fail()
    return login_v.message


@user.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        logout_user()
        login_v.logout_success()
        return login_v.message


@user.route('/login/info', methods=['GET', 'POST'])
def login_info():
    print(current_user)
    login_info = LoginInfo(current_user)
    return login_info.to_dic()







