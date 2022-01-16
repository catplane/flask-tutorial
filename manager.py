from flask_migrate import Migrate
from stitcmonster.corelib.exts import db
from stitcmonster.app import app


migrate = Migrate(app, db)