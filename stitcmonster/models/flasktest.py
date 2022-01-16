from stitcmonster.corelib.exts import db

class FlasTest(db.Model):
    __tablename__ = 'flask_test'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<FLaskTest %r>' % self.name
