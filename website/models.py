from . import db
from flask_login import UserMixin


class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_field = db.Column(db.String(100))
    salary_range = db.Column(db.Integer)
    location = db.Column(db.String(100))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

