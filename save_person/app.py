import json

def load_body(event):
    return json.loads(event['body'])

def lambda_handler(event, __):
    try:
        body = load_body(event)
        name = body.get('name')
        mail = body.get('mail')

        if not name or not mail:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Please provide a name and mail'})
            }
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Successfully saved person'})
        }
        return response
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Server failed'})
        }
