from flask import render_template, request
from flask import Blueprint

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("main.html", name=request.args["name"])
