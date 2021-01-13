# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

import os
import logging

from logging import FileHandler
from flask import Flask

from .config import DefaultConfig
from .main import main
from .admin import admin
from .personagens import personagens


__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (main, admin, personagens)


def create_app(config=None, blueprints=None):
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask('odtools')

    configure_app(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_logging(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)

    if config:
        app.config.from_object(config)


def configure_blueprints(app, blueprints):
    for module in blueprints:
        app.register_blueprint(module)


def configure_extensions(app):
    pass


def configure_logging(app):
    log_file = os.path.join(app.config['LOG_DIR'], 'application.log')

    app_log_handler = FileHandler(log_file, encoding= "UTF-8")
    app_log_handler.setLevel(logging.DEBUG)
    app_log_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    app.logger.addHandler(app_log_handler)
