from flask import Blueprint, render_template

travel_log_blue = Blueprint("travel_log_blue", __name__, url_prefix="/travel_log")


@travel_log_blue.route("/")
def travel_log():
    return render_template('travel_log.html')