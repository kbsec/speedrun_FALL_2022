from speedrun.db import db
import os 


def random_id():
    return os.urandom(16).hex()


class TestDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foo = db.Column(db.String)
    bar = db.Column(db.String)


class Implant(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    implant_id = db.Column(db.String)
    username = db.Column(db.String)
    hostname = db.Column(db.String)
    os_type = db.Column(db.String)
    os_name =db.Column(db.String)
    os_version  = db.Column(db.String)

    # todo add session crypto 

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Task(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String)
    implant_id = db.Column(db.String)
    cmd = db.Column(db.String)
    args = db.Column(db.String)
    
    status =  db.Column(db.String)

    # @TODO it would be nice to know when the job was created! when it was pulled down and when it was executed
    ##timestamp =  

