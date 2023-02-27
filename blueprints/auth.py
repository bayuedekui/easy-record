from flask import Blueprint
import models

# auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/test")
def test():
    return "hello auth"
