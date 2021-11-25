from flask import Flask
from config import Config
from app.middleware import PrefixMiddleware

application = Flask(__name__)
application.config.from_object(Config)

# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=False)

from app import routes
