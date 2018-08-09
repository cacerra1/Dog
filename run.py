from app import create_app, db
from flask_login import LoginManager
#from app.RiskAssess.old2 import Process
from sqlalchemy import exc
from flask_migrate import Migrate, Manager,  MigrateCommand

flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()

    flask_app.run(debug=False)