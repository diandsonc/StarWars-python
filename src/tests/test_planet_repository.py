from src.tests.configure_test import app, db, TestConfig
from src.api.models.planet import Planet
from src.api.repository.planet_repository import PlanetRepository
from sqlalchemy.exc import IntegrityError
import pytest


def test_create_should_persist_data(app):
    app = app(TestConfig)

    planet_alderaan = Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains")
    PlanetRepository.add(planet_alderaan)

    assert Planet.query.count() == 1


def test_list_all_should(app):
    app = app(TestConfig)
    planet_alderaan = Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains")
    planet_hoth = Planet(name="Hoth", climate="frozen",terrain="tundra, ice caves, mountain ranges")
    db.session.add(planet_alderaan)
    db.session.add(planet_hoth)
    db.session.commit()

    planets = PlanetRepository.get_all()

    assert len(planets) == 2


def test_delete_should_remove_data(app):
    app = app(TestConfig)
    planet_alderaan = Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains")
    planet_hoth = Planet(name="Hoth", climate="frozen", terrain="tundra, ice caves, mountain ranges")
    db.session.add(planet_alderaan)
    db.session.add(planet_hoth)
    db.session.commit()

    PlanetRepository.remove(planet_alderaan.id)

    assert Planet.query.count() == 1


def test_update_should_change_and_persist_data(app):
    app = app(TestConfig)

    planet_alderaan = Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains")
    db.session.add(planet_alderaan)
    db.session.commit()

    planet_alderaan.name = "Hoth"
    planet_alderaan.climate = "frozen"
    planet_alderaan.terrain = "tundra, ice caves, mountain ranges"

    PlanetRepository.update(planet_alderaan.id)
    db.session.commit()

    planet = Planet.query.get(1)

    assert planet.name == "Hoth"
    assert planet.climate == "frozen"
    assert planet.terrain == "tundra, ice caves, mountain ranges"


def test_find_by_id_should(app):
    app = app(TestConfig)
    planet_alderaan = Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains")
    planet_hoth = Planet(name="Hoth", climate="frozen", terrain="tundra, ice caves, mountain ranges")
    db.session.add(planet_alderaan)
    db.session.add(planet_hoth)
    db.session.commit()

    planet = PlanetRepository.find_by_id(planet_hoth.id)

    assert planet.name == "Hoth"


def test_find_by_name_should(app):
    app = app(TestConfig)
    planet_alderaan = Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains")
    planet_hoth = Planet(name="Hoth", climate="frozen", terrain="tundra, ice caves, mountain ranges")
    db.session.add(planet_alderaan)
    db.session.add(planet_hoth)
    db.session.commit()

    planet = PlanetRepository.find_by_name("Hoth")

    assert planet[0].name == "Hoth"


def test_create_when_name_is_null_should_throw_constraint_violate(app):
    app = app(TestConfig)

    with pytest.raises(IntegrityError) as excinfo:
        planet_alderaan = Planet(name=None, climate="temperate", terrain="grasslands, mountains")
        db.session.add(planet_alderaan)
        db.session.commit()
    db.session.rollback()


def test_create_when_climate_is_null_should_throw_constraint_violate(app):
    app = app(TestConfig)

    with pytest.raises(IntegrityError) as excinfo:
        planet_alderaan = Planet(name="Alderaan", climate=None, terrain="grasslands, mountains")
        db.session.add(planet_alderaan)
        db.session.commit()
    db.session.rollback()


def test_create_when_terrain_is_null_should_throw_constraint_violate(app):
    app = app(TestConfig)

    with pytest.raises(IntegrityError) as excinfo:
        planet_alderaan = Planet(name="Alderaan", climate="temperate", terrain=None)
        db.session.add(planet_alderaan)
        db.session.commit()
    db.session.rollback()
