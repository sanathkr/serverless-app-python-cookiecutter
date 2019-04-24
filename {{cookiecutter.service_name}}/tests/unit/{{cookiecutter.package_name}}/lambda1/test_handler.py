from unittest import TestCase

from {{cookiecutter.package_name}}.{{cookiecutter.package_name}}.lambda1.handler import lambda_handler


class TestHandler(TestCase):

    def test_handler_must_return_hello_world(self):
        self.assertEqual(lambda_handler({}, {}), {"body": "Hello World", "statusCode": 200})
