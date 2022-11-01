from flask import Blueprint
from speedrun.db import db

c2 = Blueprint('c2', __name__)



@c2.route("/index.html")
def hello_c2():
    return "Nothing to see here"
