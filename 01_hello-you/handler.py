import json

def hello(event, context):
    name_from_api_input = event['pathParameters']['name']
    http_response = {
        "statusCode": 200,
        "body": json.dumps({"hello": name_from_api_input})
    }
    return http_response