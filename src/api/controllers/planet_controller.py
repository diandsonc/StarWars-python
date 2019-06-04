from src.api.models.schemas.planet_schema import PlanetSchema
from src.api.services.planet_service import PlanetService
from src.api.util.router import Router
from src.api.util.response import Response
from flask import request
from marshmallow import pprint

router = Router('/api/v1/planets', __name__)


@router.route('', methods=['GET'])
def list_all():
    ps = PlanetSchema(many=True)
    planets = PlanetService.get_all()
    planets = ps.to_json(planets)
    return Response.ok(planets)


@router.route('/search/id/<int:id>', methods=['GET'])
def find_by_id(id):
    ps = PlanetSchema()
    result = PlanetService.find_by_id(id)

    if not result:
        return Response.not_found()

    planets = ps.to_json(result)
    return Response.ok(planets)


@router.route('/search/name/<string:name>', methods=['GET'])
def find_by_name(name):
    ps = PlanetSchema(many=True)
    planets = PlanetService.find_by_name(name)
    planets = ps.to_json(planets)
    return Response.ok(planets)


@router.route('', methods=['POST'])
def post():
    ps = PlanetSchema()
    planet, errors = ps.load(request.json)

    if errors:
        return Response.bad_request(errors, planet)

    planet = PlanetService.add(planet)
    planet = ps.to_json(planet)

    return Response.ok(planet)


@router.route('/<int:id>', methods=['PUT'])
def put(id):
    ps = PlanetSchema()
    planet, errors = ps.load(request.json)

    if errors:
        return Response.bad_request(errors, planet)

    planet_existent = PlanetService.find_by_id(id)

    if not planet_existent:
        return Response.not_found()

    planet = ps.update_object(planet, planet_existent)
    result = PlanetService.update(planet)
    result = ps.to_json(result)
    return Response.ok(result, 200)


@router.route('/<int:id>', methods=['DELETE'])
def delete(id):
    planet = PlanetService.find_by_id(id)

    if not planet:
        return Response.not_found()

    PlanetService.remove(id)
    return Response.no_content()
