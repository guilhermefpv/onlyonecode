# -*- coding: utf-8 -*-
"""Public section, including homepage."""
from datetime import datetime

from flask import (
    Blueprint,
    current_app,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)

from onlyonecode.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""

    return render_template("public/home.html")


@blueprint.route("/healthcheck/")
def healthcheck():
    """Healthcheck"""
    return "Working OK"
    # return render_template("public/healthcheck.html")


@blueprint.route("/dinamico/")
def dinamico():
    now = datetime.now()
    request_time = now.strftime("%d/%m/%Y %H:%M:%S")  # dd/mm/YY H:M:S
    # log.info(
    #     "Teste de acesso a rota default",
    #     extra={"tags": {"service": "web"}},
    # )
    return f"horário da requisição: {request_time}"


# @blueprint.route("/status/")
# def status():
#     """Status Page"""
#     #return "Working OK"
#     return render_template("public/status.html")
