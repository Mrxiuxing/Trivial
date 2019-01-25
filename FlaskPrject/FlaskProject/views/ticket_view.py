from flask import Blueprint

ticket_blue = Blueprint("ticket_blue", __name__, url_prefix="/ticket")


@ticket_blue.route("/")
def tickets():
    return "Hello Tickets"
