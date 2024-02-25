from flask import Blueprint, render_template

user = Blueprint("user", __name__)


@user.route("/", methods=["GET"])
@user.route("/home")
def home():
    """
    Render homepage.
    """
    return render_template("index.html")
