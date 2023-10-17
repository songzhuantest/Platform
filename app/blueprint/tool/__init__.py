# 通用

from flask import Blueprint

tool = Blueprint('tool', __name__)


from .view import *
