from flask import Blueprint, render_template

index_blue = Blueprint("index_blue", __name__, url_prefix="/")


@index_blue.route("/")
def index():
    return render_template('index.html', index=index)
