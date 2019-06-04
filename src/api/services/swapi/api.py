from src.api.services.swapi.exceptions import ResourceDoesNotExist
from src.api.services.swapi.models import PlanetList
from src.api.services.swapi.settings import BASE_URL, USER_AGENT_NAME
import json
import requests


def query(url):
    headers = {'User-Agent': USER_AGENT_NAME}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ResourceDoesNotExist('Resource does not exist')
    return response


def get_planet(planet_name):
    url = "{0}/planets/?search={1}".format(BASE_URL, planet_name)
    result = query(url)
    data = json.loads(result.content)
    planets = PlanetList(**data)

    for planet in planets.results:
        if planet.name == planet_name:
            return planet

    return None


def get_total_films(planet_name):
    planet = get_planet(planet_name)

    if planet is not None:
        return len(planet.films)

    return None
