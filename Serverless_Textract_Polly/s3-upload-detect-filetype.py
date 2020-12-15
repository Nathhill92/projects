import boto3, json

#Env Variables
sns = boto3.client('sns')
ses = boto3.client('ses')

# Lambda Handler / "Main"
def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        document = record['s3']['object']['key']

    extension = document[-4:]
    print(extension)

    if extension == ".pdf":
        # flag multipage function
        print("pdf file")

    elif extension == ".png" or extension == ".jpg":
        # flag for single page function
        print("jpg or png")

    elif extension == ".mp3":
        print("mp3")
        # send message to user that mp3 file is ready
        # just emails me for now   
        ses.send_email( Source='Nathanis1337@gmail.com',
            Destination={ 'ToAddresses': ["Nathanis1337"] }, 
            Message={ 'Subject': {'Data': 'Your mp3 file is now uploaded'},
                 'Body': {'Text': {'Data': "check s3 bucket"}}
            }
        )
    
    else:
        print("invalid file type")
        exit
        
    #send message to SNS
    response = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:630407588899:NotesToSpeech-FileExtension-SNS',
        Message=json.dumps(
            {
                "Data":{
                    "document":document,
                    "bucket":bucket,
                }
            }
        ),
        Subject='SpeechtoText-app',
        MessageAttributes={
            'Extension': {
                'DataType': 'String',
                'StringValue': extension
            }
        }
    )
