from flask import Flask
from stitcmonster.corelib.exts import db
from config import config
from 

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    app.register_blueprint(main_blueprint)
    # attach routes and custom error pages here

    return app