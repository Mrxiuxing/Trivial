from FlaskProject.views.index_view import index_blue
from FlaskProject.views.resume_view import resume_blue
from FlaskProject.views.travel_log_view import travel_log_blue


def init_blue(app):
    app.register_blueprint(blueprint=index_blue)
    app.register_blueprint(blueprint=resume_blue)
    app.register_blueprint(blueprint=travel_log_blue)
