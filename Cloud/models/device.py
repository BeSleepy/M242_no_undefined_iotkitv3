from db import db


class Device(db.Model):
    id_device = db.Column(db.Integer, nullable=False, primary_key=True)
    last_card_scan = db.Column(db.String(255), nullable=False)
    sensor_data = db.Column(db.String(255), nullable=False)
    fk_user = db.Column(db.Integer, db.ForeignKey("user.id_user"), nullable=False)

    def __init__(self, last_card_scan, sensor_data, fk_user):
        self.last_card_scan = last_card_scan
        self.fk_user = fk_user
        self.sensor_data = sensor_data


    def __repr__(self):
        return '<Device %r>' % self.id_device