import sys
import os.path
from unittest import TestCase
from flask import json
import unittest

source_dir = (os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')) + '/source/')
sys.path.append(source_dir)
sys.path.append("../")
from source.main import app


# sys.path.append("../")
# from source.main import app
# #from ..source.fibonacci import fibonacci_combinations


class FlaskappTests(TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_parameter_status_code_200(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fib/5')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_url_incorrect_status_code_404(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fibo/7')
        # assert the status code of the response
        self.assertEqual(result.status_code, 404)

    def test_fibonacci_list_value_5(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fib/5')
        # assert the status code of the response
        self.assertEqual(json.loads(result.data)['result'], [[2, 3], [3, 2]])

    def test_fibonacci_list_value_6(self):
        # sends HTTP GET request to the application
        result = self.app.get('/fib/6')
        # assert the status code of the response
        self.assertEqual(json.loads(result.data)['result'],
                         [[3, 3], [2, 2, 2]])


if __name__ == "__main__":
    unittest.main()