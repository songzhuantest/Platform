from flask import Flask
from flask_login import LoginManager

from app.models import db
from app.libs.email_to import mail

login_manager = LoginManager()


def register_blueprint(app):
    from app.blueprint.user import user
    app.register_blueprint(user, url_prefix='/pl/user')


def register_blueprint_device(app):
    from app.blueprint.device import device
    app.register_blueprint(device, url_prefix='/pl/device')


def register_blueprint_general(app):
    from app.blueprint.general import general
    app.register_blueprint(general, url_prefix='/pl/general')


def register_blueprint_tool(app):
    from app.blueprint.tool import tool
    app.register_blueprint(tool, url_prefix='/pl/tool')


def register_blueprint_ui(app):
    from app.blueprint.ui import ui
    app.register_blueprint(ui, url_prefix='/pl/ui')


def register_blueprint_monkey(app):
    from app.blueprint.monkey import monkey
    app.register_blueprint(monkey, url_prefix='/pl/monkey')


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting.secure')
    app.config.from_object('app.setting.setting')
    register_blueprint(app)
    register_blueprint_device(app)
    register_blueprint_general(app)
    register_blueprint_tool(app)
    register_blueprint_ui(app)
    register_blueprint_monkey(app)

    login_manager.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    return app




