import boto3, json
from datetime import datetime, timedelta

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Print event data to logs .. 
    print("Received event: " + json.dumps(event))

    # Load data coming from APIGateway
    data = json.loads(event['body'])
    
    # Generate "due time" for task
    dueValue = datetime.now() + timedelta(hours=int(data['dueValue']))
    

    # Write to DynamoDB Table - ToDoTable
    dynamodb.put_item(
        TableName='ToDoTable',
        Item={
            'task': {'S': data['task']},
            'email': {'S': data['email']},
            'due': {'S': str(dueValue)}
        }
        )

    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin":"*"},
        "body": json.dumps( {"Status": "Success"} )
        }
        
    return response
