"""
Entrypoint for all Lambda function handlers used by this service
"""

# pylint: disable=import-error, no-name-in-module
from {{cookiecutter.package_name}}.lambda1.handler import lambda_handler as lambda1_handler  # noqa
