from . import db 

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url=db.Column(db.String(200))
    video_title = db.Column(db.String(50))
    percentage = db.Column(db.Float)
    thumbnail=db.Column(db.String(200))
    description=db.Column(db.String(200))
    channel_name=db.Column(db.String(50))