from . import db

class Files(db.Model):

    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.String(100), nullable=False)
