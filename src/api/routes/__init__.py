from src.api.controllers.planet_controller import router as planet_controller


def register_blueprint(app):
    app.register_blueprint(planet_controller)
