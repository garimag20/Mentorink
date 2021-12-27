from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from database.models import db_initialiser
import os
from resources.signup_routes import signblue
from resources.login_routes import loginblue
from resources.dashboard_routes import dashblue



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database/db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db_initialiser(app)

# registering the routes in main file
app.register_blueprint(signblue)
app.register_blueprint(loginblue)
app.register_blueprint(dashblue)


app.run(debug=True)