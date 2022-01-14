import boto3


dynamodb = boto3.client('dynamodb')

def handler(event, context):
    try:
        table = dynamodb.Table('ApiKeys')
        api_key = event.pathParameters.get('apiKey')
        response = table.get_item(Key={'apiKey': api_key})
    except Exception as e:
        return generate_policy('Deny', event['methodArn'])
    else:
        return generate_policy('Allow', event['methodArn'])


def generate_policy(effect, resource):
    policy = {
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    "Effect": effect,
                    "Action": "execute-api:Invoke",
                    "Resource": resource
                }
            ]
        }
    }
    return policy
