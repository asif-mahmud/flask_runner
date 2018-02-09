"""Implementation of app factory."""

import os
import logging

import flask

from . import utils         # pylint: disable=E0401
from . import extensions    # pylint: disable=E0401
from . import db            # pylint: disable=E0401


def create_app():
    app_settings = {}
    if os.environ.get('PROD', ''):
        from .configs.production import APP_CONFIG  # pylint: disable=E0401
        app_settings = APP_CONFIG
        print('[x] Production config loaded.')
    else:
        from .configs.development import APP_CONFIG # pylint: disable=E0401
        app_settings = APP_CONFIG
        print('[x] Development config loaded.')

    app = flask.Flask(
        __package__.split('.')[0],
    )

    # update app settings
    app.config.update(app_settings)

    # register the extensions upfront
    extensions.register_extensions(app)

    # scan for model definitions
    utils.scan_models(app)

    # register blueprints
    utils.scan_blueprints(app)

    return app
