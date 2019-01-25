from FlaskProject.views.animal_view import animal_blue
from FlaskProject.views.ticket_view import ticket_blue
from FlaskProject.models import Animal


def init_blue(app):
    app.register_blueprint(blueprint=animal_blue)
    app.register_blueprint(blueprint=ticket_blue)
