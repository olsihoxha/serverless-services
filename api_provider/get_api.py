import json
import uuid

import boto3

dynamodb = boto3.client('dynamodb')


def get_key(event, context):
    table = dynamodb.Table('ApiKeys')
    event_body = json.loads(event['body'])

    email = event_body.get('email')

    try:
        response = table.get_item(Key={'email': email})
    except Exception as e:

        api_key = generate_api_key()
        response = table.put_item(Item={
            'email': email,
            'apiKey': api_key
        })
        # as per documentation put_item does not throw exceptions
        return {
            'statusCode': 201,
            'body': json.dumps({'apiKey': api_key})
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({'apiKey': response['Item']['apiKey']})
        }


def generate_api_key():
    result = uuid.uuid4()
    return result
