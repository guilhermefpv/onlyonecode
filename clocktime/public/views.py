# -*- coding: utf-8 -*-
"""Public section, including homepage/healthcheck."""
from flask import Blueprint, render_template
from datetime import datetime
from random import randrange

import requests

blueprint = Blueprint("public", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    res_time = dinamico()
    res = [randrange(1, 50, 1) for i in range(6)]
    # print("Random number list is :  +",  str(res))
    return render_template("public/home.html",
                           timestamp=res_time,
                           random_num_list=str(res))


@blueprint.route("/healthcheck/")
def healthcheck():
    """Home page."""
    return "Working OK"


@blueprint.route("/dinamico/")
def dinamico():
    """Home page."""
    now = datetime.now()
    request_time = now.strftime("%d %B %Y %I:%M:%S %p")   # "%d/%m/%Y %H:%M" dd/mm/YY H:M:S
    return f"horário da requisição: {request_time}"


# Generate Error for Test openTelemetry
@blueprint.route("/generate-error/")
def generate_error():
    """Generate Error for Test openTelemetry."""
    if randrange(10) % 2:
        response = requests.get("https://guilhermefpv.free.beeceptor.com/todos")
        response.close()
        listf = []
    elif randrange(10) % 2:
        listf()
    elif randrange(10) % 2:
        map[x] = "e23"
        for x in range(0, 3):
            map[x] = 3
            print(x)
    else:
        a3 = 100 / 0
        print(a3)
