from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = "EH$?fr3+x,&rXlgrfgsc49RWPRB55B"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TESTING'] = False
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=1)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=5)
db = SQLAlchemy(app)
db.init_app(app)
loginManager = LoginManager(app)
loginManager.login_view = 'login'
loginManager.session_protection = 'strong'
loginManager.init_app(app)


from dis_site import routes
