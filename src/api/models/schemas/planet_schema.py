from src.api import ma
from src.api.models.planet import Planet
from marshmallow import fields, validate


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
