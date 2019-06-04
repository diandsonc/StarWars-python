from src.api.models.planet import Planet
from src.api import db


class PlanetRepository():

    def get_all():
        result = Planet.query.all()

        return result

    def find_by_name(name: str):
        result = Planet.query.filter_by(name=name)

        return result

    def find_by_id(id: int):
        result = Planet.query.get(id)

        return result

    def add(planet: Planet):
        db.session.add(planet)
        db.session.commit()

        return planet

    def update(planet: Planet):
        db.session.commit()

        return planet

    def remove(id: int):
        planet = Planet.query.get(id)
        db.session.delete(planet)
        db.session.commit()