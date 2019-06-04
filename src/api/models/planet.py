from src.api import db


class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    climate = db.Column(db.String(40), nullable=False)
    terrain = db.Column(db.String(60), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    films: int

    def __init__(self, name, climate, terrain):
        self.name = name
        self.climate = climate
        self.terrain = terrain