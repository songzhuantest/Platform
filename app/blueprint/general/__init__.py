# 通用

from flask import Blueprint

general = Blueprint('general', __name__)


from .view import *

