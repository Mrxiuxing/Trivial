from flask import Blueprint

animal_blue = Blueprint("animal_blue", __name__, url_prefix="/animal")


@animal_blue.route("/")
def index():
    return "Hello Animal"
