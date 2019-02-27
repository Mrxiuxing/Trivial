from flask import Blueprint, render_template

resume_blue = Blueprint("resume_blue", __name__, url_prefix="/resume")


@resume_blue.route("/")
def resume():
    return render_template('resume.html')
