# monkey 注册

from flask import Blueprint

monkey = Blueprint('monkey', __name__)


from .monkey import *