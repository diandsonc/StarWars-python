# StarWars API   
Nossos associados são aficionados por Star Wars e com isso, queremos criar um jogo com algumas informações da franquia.

Para possibilitar a equipe de front criar essa aplicação, queremos desenvolver uma API que contenha os dados dos planetas. 

Requisitos:
- A API deve ser REST
- Para cada planeta, os seguintes dados devem ser obtidos do banco de dados da aplicação, sendo inserido manualmente:
	* Nome
	* Clima
	* Terreno
- Para cada planeta também devemos ter a quantidade de aparições em filmes, que podem ser obtidas pela API pública do Star Wars: https://swapi.co/

Funcionalidades desejadas: 

- Adicionar um planeta (com nome, clima e terreno)
- Listar planetas
- Buscar por nome
- Buscar por ID
- Remover planeta


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

flask run
```