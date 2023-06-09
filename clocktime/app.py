# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import logging
import logging.handlers
import sys

# import logging_loki
from multiprocessing import Queue

import sentry_sdk
from flask import Flask, render_template
from opentelemetry.instrumentation.wsgi import OpenTelemetryMiddleware
from sentry_sdk.integrations.flask import FlaskIntegration

from clocktime import commands, public
from clocktime.extensions import cache, debug_toolbar, flask_static_digest
from clocktime.settings import DSN_SENTRY

sentry_sdk.init(
    dsn=DSN_SENTRY,
    integrations=[
        FlaskIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    # traces_sample_rate=1.0
    profiles_sample_rate=1.0
    # Alternatively, to control sampling dynamically
    # #profiles_sampler=profiles_sampler
)


def create_app(config_object="clocktime.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    # OpenTelemetry
    app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    # register_shellcontext(app)
    register_commands(app)
    configure_logger(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    cache.init_app(app)
    debug_toolbar.init_app(app)
    flask_static_digest.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)


# class RequestIdMiddleware:
#         def __init__(self, get_response):
#             self.get_response = get_response
#
# #         def __call__(self, request):
#             # If there's an `X-Request-Id` header on the request,
#             # bind it to our Sentry SDK scope.
#             request_id = request.META.get("HTTP_X_REQUEST_ID")
#             if request_id:
#                 with sentry_sdk.configure_scope() as scope:
#                     scope.set_tag("request_id", request_id)
#             return self.get_response(request)
# # https://github.com/GreyZmeem/python-logging-loki
# def configure_logger(app):
#     """Configure logging_loki."""
##
#   # handler = logging.StreamHandler(sys.stdout)
#     handler = logging_loki.LokiQueueHandler(
#         Queue(-1),
#         url="https://loki/api/v1/push",
#         tags={"application": "clocktime-app"},
#         auth=("username", "password"),
#         version="1",
#     )
#     if not app.logger.handlers:
#         app.logger.addHandler(handler)
