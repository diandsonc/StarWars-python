class Planet(object):
    def __init__(self, name, diameter, climate, gravity, terrain, population, created, edited, url,
                 rotation_period, orbital_period, surface_water, residents, films):
        self.name = name
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.population = population
        self.created = created
        self.edited = edited
        self.url = url
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.surface_water = surface_water
        self.residents = residents
        self.films = films

    def __repr__(self):
        return '<Planet(name={self.name!r})>'.format(self=self)

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class PlanetList(object):
    def __init__(self, count, next, previous, results):
        self.count = count
        self.next = next
        self.previous = previous
        self.results = list(map(Planet.from_json, results))
