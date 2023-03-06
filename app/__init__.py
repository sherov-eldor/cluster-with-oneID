from flask_sqlalchemy import SQLAlchemy
from flask_oneid import OneID
from flask import *
from flask_login import LoginManager


oneid = OneID()

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
oneid.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


with app.app_context():
    # db.drop_all()
    db.create_all()

from app import route


with app.test_request_context():
    oneid.Set_Callback(url_for('get_params'))



