from . import db


class Thing(db.Model):
    __tablename__ = 'things'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}, name {}>'.format(self.id, self.name)

