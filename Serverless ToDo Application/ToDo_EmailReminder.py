import json, boto3
from datetime import datetime, timedelta

#open dynamoDB table and scan
client = boto3.client('dynamodb')

#ses client
ses = boto3.client('ses')

def lambda_handler(event, context):
    response = client.scan(TableName = 'ToDoTable')
    #print(response)
    
    for item in response['Items']:
        # Initialize variables
        toAddress = item['email']['S']
        emailBody = item['task']['S']
        
        # Grab time due
        dueTime = item['due']['S']
        # Format time due without nanoseconds
        dueTime = dueTime.split(".")
        
        # Convert dueTime to datetime object for timedelta object
        datetime_object = datetime.strptime(dueTime[0], "%Y-%m-%d %H:%M:%S")
    
        #how much time is left
        timeRemaining = datetime_object - datetime.now()
        
        #Checks if LESS than one hour remains - emails user if so
        if timeRemaining.seconds//3600 <= 1:
            
            # Logic for emailing user about task    
            ses.send_email( Source='Nathanis1337@gmail.com',
                Destination={ 'ToAddresses': [toAddress] }, 
                Message={ 'Subject': {'Data': 'Your task is due soon!'},
                     'Body': {'Text': {'Data': emailBody}}
                }
            )
            
        else:
            continue
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
