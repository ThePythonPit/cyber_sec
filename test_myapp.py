from flask_testing import TestCase
from app import create_app


class MyTest(TestCase):
    def create_app(self):
        # Configura la tua app per il testing
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_homepage(self):
        response = self.client.get('/')
        self.assert200(response)

def test_example_function():
    assert True


    