# user 注册

from flask import Blueprint

user = Blueprint('user', __name__, template_folder='templates/')

from . import register
from . import login
from . import person
