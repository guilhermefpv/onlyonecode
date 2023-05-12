# -*- coding: utf-8 -*-
"""Public section, including homepage/healthcheck."""

from datetime import datetime

from flask import Blueprint, render_template

blueprint = Blueprint("public", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""

    return render_template("public/home.html")


@blueprint.route("/healthcheck/")
def healthcheck():
    """Home page."""
    return "Working OK"
    # return render_template("public/healthcheck.html")


@blueprint.route("/dinamico/")
def dinamico():
    """Home page."""

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
