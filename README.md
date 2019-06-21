[![Build Status](https://travis-ci.com/diandsonc/StarWars-python.svg?branch=master)](https://travis-ci.com/diandsonc/StarWars-python)
[![codecov](https://codecov.io/gh/diandsonc/StarWars-python/branch/master/graph/badge.svg)](https://codecov.io/gh/diandsonc/StarWars-python)

# StarWars API   
API simples de cadastro de planetas com integração com https://swapi.co/. 



# API Endpoints
|Endpoint                                   | Functionality                      |HTTP method 
|-------------------------------------------|------------------------------------|-------------
|/api/v1/planets                            |Add a planet                        |POST        
|/api/v1/planets/*planet_id*                |modify a planet’s information       |PUT
|/api/v1/planets/*planet_id*                |Remove a planet                     |DELETE
|/api/v1/planets                            |Retrieves all planets               |GET
|/api/v1/planets/search/id/*planet_id*      |Search a planet by id               |GET
|/api/v1/planets/search/name/*planet_name*  |Search a planet by name             |GET


# Installing Application and Running
Install virtual env requests: `py -m venv env`

Install all the dependencies through: `pip install -r requirements.txt`

Activate the virtual environment: `source env/Scripts/activate`


# Running Application
```sh
export FLASK_APP=run.py
export FLASK_ENV=development
export FLASK_DEBUG=True
export DATABASE_URL='sqlite:////production_starWars.db'
export PRODUCTION=True

flask run
```


# Running tests      
To run test, use: `pytest`


# Migration
```sh
flask db init
flask db migrate
flask db upgrade
flask db downgrade
```

To generate script `--sql`

To define migrate target `--tag`
