# user model
from random import sample

from itsdangerous import TimedSerializer
from sqlalchemy import Column, Integer, String, SmallInteger

import app
from app.libs.enums import RoleStatus
from app.models.base import Base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# def nickname_rand():
#     return '帮帮选手' + "".join(sample('12345', 5))


class User(Base, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    _nickname = Column('nickname', String(50), nullable=False, default='12324')
    _role = Column('role', SmallInteger, default='4')
    _password = Column('password', String(150), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @property
    def role(self):
        return RoleStatus(self._role)

    @role.setter
    def role(self, role):
        return role.value

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, raw):
        self._nickname = raw

    def is_same_password(self, password):
        return check_password_hash(self._password, password)

    # def generate_token(self, expiration=600):
    #     from app.manage import app
    #     s = TimedSerializer(app.config['SECRET_KEY'])
    #     temp = s.dumps(self.id)
    #     return temp


@app.login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

