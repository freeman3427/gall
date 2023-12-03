from app import db


class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Coment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gall_id = db.Column(db.Integer, db.ForeginKey(
        'gallery.id', ondelete='CASCADE'))
    gall = db.relationship('Gallery', backref=db.backref('coment_set'))
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
