import os

from flask import (  # Response,
    Blueprint,
    render_template,
    send_from_directory,
)
from werkzeug import Response

bp = Blueprint(
    "app",
    __name__,
    static_folder="app/static",
    template_folder="app/templates",
)


@bp.route("/favicon.ico")
def favicon() -> Response:
    return send_from_directory(
        os.path.join(bp.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@bp.route("/")
def index() -> str:
    return render_template(
        "index.html",
    )
