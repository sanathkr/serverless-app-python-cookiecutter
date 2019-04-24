"""
Actual Lambda function handler
"""


def lambda_handler(event, context):
    return {"body": "Hello World", "statusCode": 200}
