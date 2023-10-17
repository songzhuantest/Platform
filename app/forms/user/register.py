from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, length, Length


class RegisterForm(Form):
    nickname = StringField(name='nickname', validators=[Email(), Length(1, 254)])
    password = StringField(name='password', validators=[Length(min=6, max=20)])

    # def validate_username():
    #     if User.query.filter_by(email=username.data).first():
    #         return False


if __name__ == '__main__':
    form = RegisterForm({"username": "dfsfsdf@qq.com", "password": "123456", "module": "register"})
    print(form.validate())