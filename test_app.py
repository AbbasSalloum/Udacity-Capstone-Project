import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Movie, Actor

class CapstoneTestCase(unittest.TestCase):

	def setUp(self):
		self.app = create_app()
		self.client = self.app.test_client
		self.database_name = "capstone_test"
		self.database_path = "postgres:///{}".format(self.database_name)
		setup_db(self.app, self.database_path)

		# binds the app to the current context
		with self.app.app_context():
			self.db = SQLAlchemy()
			self.db.init_app(self.app)
			# create all tables
			self.db.create_all()
	
	def tearDown(self):
		"""Executed after reach test"""
		pass

	def test_get_movies(self):
		res = self.client().get('/movies')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)
		self.assertTrue(data['success'])
		self.assertEqual(type(data["movies"]), type([]))
		self.assertEqual(len(data["movies"]), 4)

	def test_get_actors(self):
		res = self.client().get('/actors')
		data = json.loads(res.data)

		self.assertEqual(res.status_code, 200)
		self.assertTrue(data['success'])
		self.assertEqual(type(data["actors"]), type([]))
		self.assertEqual(len(data["actors"]), 5)

	

# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()