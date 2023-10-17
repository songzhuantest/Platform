# base model
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

# OverWrite SQLALchemy
from sqlalchemy import Column, SmallInteger, Integer, BigInteger, String


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_to_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column(String(50), default='1970131400')

    def __init__(self):
        self.create_time = str(int(datetime.now().timestamp()))

    def set_attrs(self, attrs_dict: dict):
        print(attrs_dict)
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)