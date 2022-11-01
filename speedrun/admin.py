from flask import Blueprint
from speedrun.db import db

admin = Blueprint('admin', __name__)



@admin.route("/admin/hello")
def hello_admin():
    return "Hello Admin!"
