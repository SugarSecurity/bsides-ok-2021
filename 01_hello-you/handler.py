import json


def hello(event, context):
    name_from_api_input = event['pathParameters']['name']
    body = {
        "hello": name_from_api_input
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
