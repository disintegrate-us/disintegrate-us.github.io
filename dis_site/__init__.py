from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = "EH$?fr3+x,&rXlgrfgsc49RWPRB55B"

from dis_site import routes
