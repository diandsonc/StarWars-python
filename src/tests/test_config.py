from src.tests.configure_test import app
from config import TestConfig, DevConfig, ProdConfig
import os


def test_development_config(app):
    app = app(DevConfig)
    DB_URL = DevConfig.SQLALCHEMY_DATABASE_URI
    assert app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL


def test_testing_config(app):
    app = app(TestConfig)
    DB_URL = TestConfig.SQLALCHEMY_DATABASE_URI
    assert app.config["DEBUG"]
    assert app.config["TESTING"]
    assert not app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL


def test_production_config(app):
    app = app(ProdConfig)
    DB_URL = ProdConfig.SQLALCHEMY_DATABASE_URI
    assert not app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL