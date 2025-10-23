from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String, nullable=False)
    transcript = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    action_items = db.Column(db.Text, nullable=False)
