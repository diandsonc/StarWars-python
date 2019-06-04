from src.api.services.swapi.api import get_total_films, get_planet, query
from src.api.services.swapi.models import Planet
from src.api.services.swapi.exceptions import ResourceDoesNotExist
from src.api.services.swapi.settings import BASE_URL
import pytest


def test_get_total_films_on_planet():
    total = get_total_films('Alderaan')

    assert total is not None
    assert type(total), int


def test_get_total_films_on_planet_not_found():
    total = get_total_films('Jupiter')

    assert total is None


def test_get_planet_by_name():
    planet = get_planet('Alderaan')

    assert planet is not None
    assert type(planet), Planet
    assert "<Planet(name='Alderaan')>" == planet.__repr__()


def test_get_planet_by_name_not_found():
    planet = get_planet('Jupiter')

    assert planet is None


def test_raise_deliberate_exception():
    with pytest.raises(ResourceDoesNotExist) as excinfo:
        result = query('{0}/planets/{1}'.format(BASE_URL, 123456))
