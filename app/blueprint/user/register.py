#  register  route
from flask import request
from werkzeug.datastructures import ImmutableMultiDict

from . import user
from ...forms.user.register import RegisterForm
from ...libs.email_to import email
from ...libs.request_to import request_form, request_to
from ...models.user.user import User
from app.models.base import db
from ...view_model.user.register import RegisterModel
register = RegisterModel()
email = email()
users = User()
code = ''


@user.route('/getsms', methods=['GET', 'POST'])
def getsms():
    if request.method == 'POST':
        request_to(request).to_get_data()
        req = request_to.to_multidict(request_form.data)
        form = RegisterForm(req)
        user = users.query.filter_by(nickname=form.data.get('nickname')).first()
        if form.validate():
            if email.send_email(request_form.data.get('nickname')):
                email.into_code(email.code)
                register.send_success()
            else:
                register.send_fail()
        else:
            register.sms_fail()
        return register.message


@user.route('/register', methods=['GET', 'POST'])
def register_to():
    from app.manage import app
    if request.method == 'POST':
        request_to(request).to_get_data()
        user = User.query.filter_by(_nickname=request_form.data.get('nickname')).first()
        if email.code_compare(app.config['ROCK_CODE'], request_form.data.get('code')) and not user:
            register.register_success()
            users.set_attrs(request_form.data)
            db.session.add(users)
            db.session.commit()
        else:
            register.register_fail()
    return register.message




