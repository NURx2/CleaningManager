from src.database import db


class Executor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    telegram_id = db.Column(db.String)
