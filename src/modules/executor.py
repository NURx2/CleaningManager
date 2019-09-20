from src.database import db


class Executor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    telegram_id = db.Column(db.String(32))
    # db.session.add(my_object)
