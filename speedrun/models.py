
from speedrun.db import db
import os 
from dataclasses import dataclass, asdict
import json



def random_id():
    return os.urandom(16).hex()

@dataclass
class TestDB(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    foo: str = db.Column(db.String)
    bar: str = db.Column(db.String)
    def toJSON(self):
        return asdict(self)

@dataclass
class Implant(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    implant_id : str = db.Column(db.String)
    username : str = db.Column(db.String)
    hostname : str = db.Column(db.String)
    os_type : str = db.Column(db.String)
    os_name : str =db.Column(db.String)
    os_version :str  = db.Column(db.String)
    # todo add session crypto 
    def toJSON(self):
        return asdict(self)

CREATED = "CREATED"
TASKED = "TASKED"
COMPLETE = "COMPLETE"
ERROR = "ERROR"

@dataclass
class Task(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    task_id : str = db.Column(db.String)
    implant_id : str = db.Column(db.String)
    cmd : str = db.Column(db.String)
    args : str = db.Column(db.String)
    
    status : str =  db.Column(db.String)
    
    # @TODO it would be nice to know when the job was created! when it was pulled down and when it was executed
    ##timestamp =  
    def toJSON(self):
        return asdict(self)
