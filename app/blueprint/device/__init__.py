# 设备

from flask import Blueprint

device = Blueprint('device', __name__)


from .view import *
from .cloud import *
