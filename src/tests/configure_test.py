from src.api import create_app, db
from src.api.models import tables as create_tables
from config import TestConfig
import pytest


@pytest.yield_fixture
def app():
    def _app(config_class):
        app = create_app(config_class)
        app.test_request_context().push()

        db.init_app(app)

        if config_class is TestConfig:
            db.drop_all()
            create_tables()
            db.create_all()

        return app

    yield _app
    db.session.remove()
