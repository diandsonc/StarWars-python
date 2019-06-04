from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow
from config import DevConfig, ProdConfig
import os


def create_app(config_object=DevConfig):
    app = Flask(__name__)

    if os.environ["PRODUCTION"] == "True":
        config_class = ProdConfig

    app.config.from_object(config_object)
    return app


def config_db(app, db):
    migrate = Migrate(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager


app = create_app()
ma = Marshmallow(app)
db = SQLAlchemy(app)
manager = config_db(app, db)
