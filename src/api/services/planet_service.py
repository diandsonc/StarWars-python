from src.api.models.planet import Planet
from src.api.repository.planet_repository import PlanetRepository


class PlanetService(PlanetRepository):

    def get_all():
        return PlanetRepository.get_all()

    def find_by_name(name: str):
        return PlanetRepository.find_by_name(name)

    def find_by_id(id: int):
        return PlanetRepository.find_by_id(id)

    def add(planet: Planet):
        return PlanetRepository.add(planet)

    def update(planet: Planet):
        return PlanetRepository.update(planet)

    def remove(id: int):
        PlanetRepository.remove(id)
