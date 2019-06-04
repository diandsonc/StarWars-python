from src.api import ma
from src.api.models.planet import Planet
from src.api.services.swapi.api import get_total_films
from marshmallow import fields, validate, post_dump


class PlanetSchema(ma.ModelSchema):
    id = fields.Integer(dump_only=True)

    name = fields.String(required=True, 
                        error_messages={'required': 'Campo nome é obrigatório!'},
                        validate={
                             validate.Length(min=1, error='Campo não pode ser vazio!'),
                             validate.Length(max=60, error='Campo não pode ter mais que 60 caracteres!')
                        })

    terrain = fields.String(required=True, 
                            error_messages={'required': 'Campo clima é obrigatório!'},
                            validate={
                                validate.Length(min=1, error='Campo não pode ser vazio!'),
                                validate.Length(max=60, error='Campo não pode ter mais que 60 caracteres!')
                            })

    climate = fields.String(required=True, 
                            error_messages={'required': 'Campo terreno é obrigatório!'},
                            validate={
                                validate.Length(min=1, error='Campo não pode ser vazio!'),
                                validate.Length(max=40, error='Campo não pode ter mais que 40 caracteres!')
                            })

    films = fields.Integer(dump_only=True)

    class Meta:
        model = Planet
        exclude = ['creation_date']

    @post_dump
    def set_value(self, data):
        data['films'] = get_total_films(data['name'])

    def to_json(self, json):
        return self.jsonify(json).json

    def update_object(selff, newObject: Planet, planet: Planet):
        planet.name = newObject.name
        planet.terrain = newObject.terrain
        planet.climate = newObject.climate
        return planet
