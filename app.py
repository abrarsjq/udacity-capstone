import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie


def create_app(test_config=None):
    # configure the app with the endpoints and return it

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')

        return response

    # Endpoint to retrieve all actors
    @app.route('/actors')
    def get_actors():
        actors = Actor.query.all()
        if len(actors) == 0:
            # abort the request, becasue no record retrieved
            abort(404)

        return jsonify({'success': True, 'actors':
                       [actor.format() for actor in actors]})

    # Endpoint to delete actor with requested ID
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    def delete_actor(actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            # abort the request, becasue no actor with that ID
            abort(404)

        actor.delete()

        return jsonify({'success': True, 'actor_id': actor_id})

    # Endpoint to add new actor to the database
    @app.route('/actors', methods=['POST'])
    def create_actor():
        data = request.get_json()

        if 'name' not in data:
            # if name not exist in the request body, abort
            abort(400)
        if 'age' not in data:
            # if age not exist in the request body, abort
            abort(400)
        if 'gender' not in data:
            # if gender not exist in the request body, abort
            abort(400)

        actor = Actor(name=data['name'],
                      gender=data['gender'],
                      age=data['age'])
        actor.insert()

        return jsonify({'success': True,
                        'actor': actor.format(),
                        'actor_id': actor.id})

    # Endpoint to edit the data of existing actor
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    def edit_actor(actor_id):
        data = request.get_json()

        actor = Actor.query.get(actor_id)

        if actor is None:
            # abort the request, becasue no actor with that ID
            abort(404)

        # if one of these property exist, mean we need to update
        if 'name' in data:
            actor.name = data['name']

        if 'gender' in data:
            actor.gender = data['gender']

        if 'age' in data:
            actor.age = data['age']

        # update the database record
        actor.update()

        return jsonify({'success': True,
                        'actor': actor.format(),
                        'actor_id': actor_id})


    # Endpoint to retrieve all movies
    @app.route('/movies')
    def get_movies():
        movies = Movie.query.all()

        # abort the request, becasue no record retrieved
        if len(movies) == 0:
            abort(404)

        return jsonify({'success': True,
                       'movies': [movie.format() for movie in movies]})

    # Endpoint to delete movie with requested ID
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movie(movie_id):
        movie = Movie.query.get(movie_id)

        if movie is None:
            # abort the request, becasue no movie with that ID
            abort(404)

        movie.delete()

        return jsonify({'success': True, 'movie_id': movie_id})

    # Endpoint to add new movie to the database
    @app.route('/movies', methods=['POST'])
    def create_movie():
        data = request.get_json()

        if 'title' not in data:
            # if movie title not exist in the request body, abort
            abort(400)
        if 'release' not in data:
            # if release date not exist in the request body, abort
            abort(400)

        movie = Movie(title=data['title'], release=data['release'])
        movie.insert()

        return jsonify({'success': True,
                        'movie': movie.format(),
                        'movie_id': movie.id})

    # Endpoint to edit the data of existing movie
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def edit_movie(movie_id):
        data = request.get_json()

        movie = Movie.query.get(movie_id)

        if movie is None:
            # abort the request, becasue no movie with that ID
            abort(404)

        # if one of these property exist in the request, mean we need to update
        if 'title' in data:
            movie.title = data['title']

        if 'release' in data:
            movie.release = data['release']

        # update the database record
        movie.update()

        return jsonify({'success': True,
                        'movie': movie.format(),
                        'movie_id': movie_id})


    @app.errorhandler(404)
    def not_found(error):
        return (jsonify({'success': False,
                         'error': 404,
                         'message': 'resource not found'}),
                404)

    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({'success': False,
                         'error': 400,
                         'message': 'bad request'}),
                400)

    @app.errorhandler(401)
    def unauthorized(error):
        return (jsonify({'success': False,
                         'error': 401,
                         'message': 'unauthorized access'}),
                401)

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)