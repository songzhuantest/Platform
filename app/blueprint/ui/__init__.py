# UI

from flask import Blueprint

ui = Blueprint('ui', __name__)


from .regression import *
