from db import db


class User(db.Model):
    id_user = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    card_uid = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, username, password, card_uid):
        self.username = username
        self.password = password
        self.card_uid = card_uid

    def __repr__(self):
        return '<User %r>' % self.username