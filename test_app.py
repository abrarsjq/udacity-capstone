import json
import os
import unittest
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

# this is the header tokens from the setup.sh
director_header = {
                            'Authorization': 'Bearer {}'.format(
                                            os.environ[
                                                'DIRECTOR']
                                            )}
producer_header = {
                            'Authorization': 'Bearer {}'.format(
                                            os.environ[
                                                'PRODUCER']
                                            )}
# smaple actor and movie object for testing
actor_sample = {'name': 'Mazin Hayek',
                'age': 23,
                'gender': 'male'}

movie_sample = {'title': 'Queen Gamblit',
                'release': "12-11-20"}

class TestAgencyAPI(unittest.TestCase):


    def setUp(self):

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'agency_test'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(
                             'postgres', 'admin',
                             'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()



        # inserting these records in the test database
        # becuase at the initiate will be empty 
        i = 0
        while i < 5:
            actor = Actor(name=actor_sample['name'],
                          age=actor_sample['age'],
                          gender=actor_sample['gender'])
            actor.insert()
            movie = Movie(title=movie_sample['title'],
                          release=movie_sample['release'])
            movie.insert()
            i += 1


    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_insert_movie_success(self):
        # producer, have all permissions, so it will return success test

        response = self.client().post(
                                      '/movies',
                                      headers=producer_header,
                                      json=movie_sample)
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_insert_movie_failure(self):
        # this test, not include token, so 401 error arise and test fail

        response = self.client().post(
                                 '/movies',
                                 headers=director_header,
                                 json=movie_sample)
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)

    def test_delete_movie_success(self):
        # producer, have all permissions, so it will return success test

        movie = Movie.query.all()[0]
        response = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=producer_header)
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_delete_movie_failure(self):
        # this test, not include token, so 401 error arise and test fail

        movie = Movie.query.all()[0]
        response = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=director_header)
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)

    def test_patch_movies_success(self):
        # producer, have all permissions, so it will return success test

        movie = Movie.query.all()[0]
        response = self.client().patch('/movies/{}'.format(movie.id),
                                       headers=producer_header,
                                       json=movie_sample)
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_patch_movies_failure(self):
        # this test, not include token, so 401 error arise and test fail

        movie = Movie.query.all()[0]
        response = self.client().patch('/movies/{}'.format(movie.id),
                                       json=movie_sample)
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)

    def test_insert_actor_success(self):
        # producer, have all permissions, so it will return success test

        response = self.client().post('/actors',
                                      headers=producer_header,
                                      json=actor_sample)
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_insert_actor_failure(self):
        # this test, not include token, so 401 error arise and test fail

        response = self.client().post('/actors', json=actor_sample)
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)

    def test_delete_actor_success(self):
        # producer, have all permissions, so it will return success test

        actor = Actor.query.all()[0]
        response = self.client().delete('/actors/{}'.format(actor.id),
                                        headers=producer_header)
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_delete_actor_failure(self):
        # this test, not include token, so 401 error arise and test fail

        actor = Actor.query.all()[0]
        response = self.client().delete('/actors/{}'.format(actor.id))
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)

    def test_patch_actor_success(self):
        # producer, have all permissions, so it will return success test

        actor = Actor.query.all()[0]
        response = self.client().patch('/actors/{}'.format(actor.id),
                                       headers=producer_header,
                                       json=actor_sample)
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_patch_actor_failure(self):
        # this test, not include token, so 401 error arise and test fail

        actor = Actor.query.all()[0]
        response = self.client().patch('/actors/{}'.format(actor.id),
                                       json=actor_sample)
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)

    def test_get_movies_success(self):
        # PUBLIC ENDPOINT, no need for tokens and it will success

        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_get_actors_success(self):
        # PUBLIC ENDPOINT, no need for tokens and it will success

        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
