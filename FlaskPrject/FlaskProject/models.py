from FlaskProject.extension import db


class Animal(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    a_name = db.Column(db.String(32))
