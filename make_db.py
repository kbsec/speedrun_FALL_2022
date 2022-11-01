from speedrun.buildapp import init_db, db
from speedrun.app import app



with app.app_context():
    init_db()
