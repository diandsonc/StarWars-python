from src.tests.configure_test import app, db, TestConfig
from src.api.models.planet import Planet
from src.api.services.swapi.models import Planet as PlanetSwapi
from mock.mock import call, patch
from types import SimpleNamespace
import json


def setup_data():
    planet_alderaan = Planet(name='Alderaan', climate='temperate', terrain='grasslands, mountains')
    planet_hoth = Planet(name='Hoth', climate='frozen', terrain='tundra, ice caves, mountain ranges')
    db.session.add(planet_alderaan)
    db.session.add(planet_hoth)
    db.session.commit()


def headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


def get_planet(name):
    return PlanetSwapi(
        name=name,
        diameter='12500',
        climate='temperate',
        gravity='1 standard',
        terrain='grasslands, mountains',
        population='2000000000',
        created=None,
        edited=None,
        url=None,
        rotation_period='24',
        orbital_period='364',
        surface_water='40',
        residents=['5', '6', '8'],
        films=['movie1', 'movie2', 'movie3']
    )


@patch('src.api.services.swapi.api.get_planet', return_value=get_planet('Alderaan'))
def test_list_planets_should_return_status_code_200(mock_get_planet, app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()

    url = '/api/v1/planets'
    response = client.get(url, headers=headers())

    mock_get_planet.assert_has_calls([call('Alderaan'), call('Hoth')])
    assert response.status_code == 200


@patch('src.api.services.swapi.api.get_planet', return_value=get_planet('Alderaan'))
def test_get_planet_by_name_should_return_status_code_200(mock_get_planet, app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()
    url = '/api/v1/planets/search/name/Alderaan'
    response = client.get(url, headers=headers())

    mock_get_planet.assert_called_once_with('Alderaan')
    assert response.status_code == 200


@patch('src.api.services.swapi.api.get_planet', return_value=get_planet('Alderaan'))
def test_get_planet_by_id_should_return_status_code_200(mock_get_planet, app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()
    url = '/api/v1/planets/search/id/1'
    response = client.get(url, headers=headers())

    mock_get_planet.assert_called_once_with('Alderaan')
    assert response.status_code == 200


@patch('src.api.services.swapi.api.get_planet', return_value=get_planet('Alderaan'))
def test_get_planet_by_id_return_json_with_filled_model(mock_get_planet, app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()
    url = '/api/v1/planets/search/id/1'
    response = client.get(url, headers=headers())
    data = json.loads(response.data, object_hook=lambda d: SimpleNamespace(**d)).data

    assert 1 == data.id
    assert 3 == data.films
    assert 'Alderaan' == data.name
    assert 'temperate' == data.climate
    assert 'grasslands, mountains' == data.terrain


def test_get_planet_by_id_when_planet_does_not_exists_should_return_status_code_404(app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()
    url = '/api/v1/planets/search/id/3'
    response = client.get(url, headers=headers())

    assert response.status_code == 404


def test_delete_planet_by_id_should_return_status_code_204(app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()
    url = '/api/v1/planets/1'
    response = client.delete(url, headers=headers())

    assert response.status_code == 204


def test_delete_planet_by_id_should_return_status_code_404(app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()

    url = '/api/v1/planets/3'
    response = client.delete(url, headers=headers())

    assert response.status_code == 404


@patch('src.api.services.swapi.api.get_planet', return_value=get_planet('Alderaan'))
def test_create_shoud_persist_data_and_return_status_code_200(mock_get_planet, app):
    app = app(TestConfig)
    client = app.test_client()
    planet = {
        'name': 'Alderaan',
        'climate': 'temperate',
        'terrain': 'grasslands, mountains'
    }
    url = '/api/v1/planets'
    response = client.post(url, data=json.dumps(planet), headers=headers())

    mock_get_planet.assert_called_once_with('Alderaan')
    assert response.status_code == 200


def test_create_when_name_is_null_shoud_return_status_code_400_bad_request(app):
    app = app(TestConfig)
    client = app.test_client()
    planet = {
        'name': None,
        'climate': 'frozen',
        'terrain': 'tundra, ice caves, mountain ranges'
    }
    url = '/api/v1/planets'
    response = client.post(url, data=json.dumps(planet), headers=headers())

    assert response.status_code == 400


def test_create_when_climate_is_null_shoud_return_status_code_400_bad_request(app):
    app = app(TestConfig)
    client = app.test_client()
    planet = {
        'name': 'Hoth',
        'climate': None,
        'terrain': 'tundra, ice caves, mountain ranges'
    }
    url = '/api/v1/planets'
    response = client.post(url, data=json.dumps(planet), headers=headers())

    assert response.status_code == 400


def test_create_when_terrain_is_null_shoud_return_status_code_400_bad_request(app):
    app = app(TestConfig)
    client = app.test_client()
    planet = {
        'name': 'Hoth',
        'climate': 'frozen',
        'terrain': None
    }
    url = '/api/v1/planets'
    response = client.post(url, data=json.dumps(planet), headers=headers())

    assert response.status_code == 400


@patch('src.api.services.swapi.api.get_planet', return_value=get_planet('Alderaan'))
def test_update_should_persist_data_and_return_status_code_200(mock_get_planet, app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()
    planet = {
        'name': 'Alderaan',
        'climate': 'temperate',
        'terrain': 'grasslands, mountains'
    }
    url = '/api/v1/planets/2'
    response = client.put(url, data=json.dumps(planet), headers=headers())

    mock_get_planet.assert_called_once_with('Alderaan')
    assert response.status_code == 200


def test_update_when_name_is_null_shoud_return_status_code_400_bad_request(app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()
    planet = {
        'name': None,
        'climate': 'frozen',
        'terrain': 'tundra, ice caves, mountain ranges'
    }
    url = '/api/v1/planets/2'
    response = client.put(url, data=json.dumps(planet), headers=headers())

    assert response.status_code == 400


def test_update_when_climate_is_null_shoud_return_status_code_400_bad_request(app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()
    planet = {
        'name': 'Hoth',
        'climate': None,
        'terrain': 'tundra, ice caves, mountain ranges'
    }
    url = '/api/v1/planets/2'
    response = client.put(url, data=json.dumps(planet), headers=headers())

    assert response.status_code == 400


def test_update_when_terrain_is_null_shoud_return_status_code_400_bad_request(app):
    app = app(TestConfig)
    client = app.test_client()
    setup_data()
    planet = {
        'name': 'Hoth',
        'climate': 'frozen',
        'terrain': None
    }
    url = '/api/v1/planets/2'
    response = client.put(url, data=json.dumps(planet), headers=headers())

    assert response.status_code == 400


def test_update_when_id_not_found_shoud_return_status_code_404_not_found(app):
    app = app(TestConfig)
    client = app.test_client()
    planet = {
        'name': 'Hoth',
        'climate': 'frozen',
        'terrain': 'tundra, ice caves, mountain ranges'
    }
    url = '/api/v1/planets/2'
    response = client.put(url, data=json.dumps(planet), headers=headers())

    assert response.status_code == 404
