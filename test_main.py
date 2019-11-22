'''
Tests for jwt flask app.
'''
import os
import json
import unittest

import main

SECRET = 'TestSecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjEzMDY3OTAsIm5iZiI6MTU2MDA5NzE5MCwiZW1haWwiOiJ3b2xmQHRoZWRvb3IuY29tIn0.IpM4VMnqIgOoQeJxUbLT-cRcAjK41jronkVrqRLFmmk'
EMAIL = 'wolf@thedoor.com'
PASSWORD = 'huff-puff'

# @pytest.fixture
class ProjectTesCase(unittest.TestCase):
    def setUp(self):
        os.environ['JWT_SECRET'] = SECRET
        main.APP.config['TESTING'] = True
        self.client = main.APP.test_client()



    def test_health(self):
        response = self.client.get('/')
        assert response.status_code == 200
        assert response.json == 'Healthy'


    def test_auth(self):
        body = {'email': EMAIL,
                'password': PASSWORD}
        response = self.client.post('/auth', 
                            data=json.dumps(body),
                            content_type='application/json')

        assert response.status_code == 200
        token = response.json['token']
        assert token is not None
