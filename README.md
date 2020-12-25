# Full Stack Nanodegree Casting Agency Capstone Project

This the project of Udacity capstone FSND, where here I will demonstrate all what i have learned in this project by implmenting it. it's challenging project, but its enjoyable one also. In this project i have build a backend service using Flask micro-framework, which is a python based framework to build backend servers. Also i have deployed my project on Heruko.  

## Getting Started

### Installing Dependencies

To run the project successfully, you will need the following tools:
1. Python3
2. PIP

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

After activating your virtualenv, you can run the following command:

```bash
pip install -r requirements.txt
```

It will install all the libraries you need from `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server locally in development environment

To run the server, execute:

```bash
pip install -r requirements.txt
source setup.sh
python app.py
```

#### Testing

To run the tests:
```
dropdb capstone_test
createdb capstone_test
source setup.sh
python test_app.py
```

## API Reference

### Introduction

For the casting agency capstone, all the endpoints will have responses in JSON format. It have been build using python Flask micro-framework.

### Getting Started

#### Base URL

The Heroku deployed application is on the URL:
```
https://agency-abrar.herokuapp.com
```

### Error

The API errors are consistant with known errors, such as the following:

#### Error Types:

- 404 - Not Found
- 422 - Unprocesaable
- 400 - Bad Request
- 401 - Unauthorized

#### Error Response Example:

```
{
    "success": False,
    "error": 404,
    "message": "Resource Not Found"
}
```

### Endpoints Library

This is the section, where we will provide you with all the API endpoints we have, also with sample examples.

#### GET /actors

- Return: return list of actors.
- Sample Request: ```curl https://agency-abrar.herokuapp.com/actors```
- Arguments: None
- Sample Response:
    ```
    {
          "success": True,
          "actors": [
            {
              "id": 1,
              "name": "Abrar Salem",
              "gender": "female",
              "age": 45
            }, 
            {
              "id": 5,
              "name": "Muslim Hadi",
              "gender": "female",
              "age": 95
            }
          ]
    }
    ```
#### GET /movies

- Return: return list of all the available movies.
- Sample Request: ```curl https://agency-abrar.herokuapp.com/movies```
- Arguments: N/A
- Sample Response:
    ```
    {
          "success": True,
          "movies": [
            {
              "id": 1,
              "title": "Queen Gamblit",
              "release": "10-09-20"
            }, 
            {
              "id": 4,
              "title": "Bruslie",
              "release": "08-11-20"
            }
          ]
    }
    ```

#### DELETE /actors/id

- Return: 
    - deleted actor id and result of success.
- Sample Request: ```curl -X "DELETE" https://agency-abrar.herokuapp.com/actors/2```
- Arguments: 
    - it take the id of the actor in the URL after the ```actors/```
- Required Headers:
    - Require Bearer Token: JWT.
- Sample Response:
    ```
    {
        "success": True,
        "actor_id": 2
    }
    ```

#### DELETE /movies/id

- Return: 
    - the deleted movie ID and result of success.
- Sample Request: ```curl -X "DELETE" https://agency-abrar.herokuapp.com/movies/5```
- Arguments: 
    - it take the id of the movie in the URL after the ```movies/```
- Required Headers:
    - Require Bearer Token: JWT.
- Sample Response:
    ```
    {
        "success": True,
        "movie_id": 2
    }
    ```

#### POST /actors

- Return: 
    - the request success message.
    - the created actor data.
    - the id of the created actor.
- Sample Request: 
    ```curl -d '{"name": "Abrar Salem", "age": 22, "gender": "female"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "POST" https://agency-abrar.herokuapp.com/actors```
- Arguments: N/A
- Required Headers:
    - Require Bearer Token: JWT.
    - Content-Type: application/json
- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 2,
            "name": "Abrar Salem",
            "gender": "female",
            "age": 22
        },
        "actor_id": 45
    }
    ```

#### POST /movies

- Return: 
    - the request success state.
    - the created movie object.
    - the ID of the created movie.

- Sample Request: 
    ```curl -d '{"title": "Queen Gamblit", "release":"10-20-20"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "POST" https://agency-abrar.herokuapp.com/movies```
- Arguments: N/A
- Required Headers:
    - Require Bearer Token: JWT.
    - Content-Type: application/json
- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 36,
            "title": "Queen Gamblit",
            "release": "10-20-20"
        },
        "movie_id": 99
    }
    ```

#### PATCH /actors

- Return:
    - the request success state.
    - the modified actor object.
    - the ID of the modified actor.
- Sample Request: 
    ```curl -d '{"name": "Abrar Salem", "age": 33, "gender": "female"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://agency-abrar.herokuapp.com/actors/8```
- Arguments: 
    - the ID of the actor that need to modified.
- Required Headers:
    - Require Bearer Token: JWT.
    - Content-Type: application/json
- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 11,
            "name": "Abrar Salem",
            "gender": "female",
            "age": 23
        },
        "actor_id": 99
    }
    ```

#### PATCH /movies

- Return:
    - the request success state.
    - the modified movie object.
    - the ID of the modified movie.
- Sample Request: 
    ```curl -d '{"title": "World war"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://agency-abrar.herokuapp.com/movies/36```
- Arguments: 
    - the ID of the movie that need to modified.
- Required Headers:
    - Require Bearer Token: JWT.
    - Content-Type: application/json
- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 28,
            "title": "World war",
            "release": "07-02-21"
        },
        "movie_id": 24
    }
    ```

## Authentication and Permissions

Authentication is handled via [Auth0](https://auth0.com).

In the project, their are two Roles:

- Casting Director:
    * 'delete:actor': delete actor from the database.
    * 'patch:actor': modify actor attributes in the database.
    * 'patch:movie': modify actor attributes in the database.
    * 'post:actors': create new actors in the database.

- Executive Director:
    * with all the permissions that Casting Director have, including:
    * 'delete:movie': delete movie from the database.
    * 'post:movies': create movies in the database.

All endpoints require authentication, and proper permission. Except the GET/actors and GET/movies are the public endpoints. So, anyone can access and retrieve information.