from speedrun.db import db



class TestDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foo = db.Column(db.String)
    bar = db.Column(db.String)


    