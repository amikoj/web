# !/usr/bin/env python
# -*-coding:utf-8-*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    # 注册蓝本
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .share import share as share_blueprint
    app.register_blueprint(share_blueprint,url_prefix='/share')

    # api
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint,url_prefix='/api/v1.0')

    return app


