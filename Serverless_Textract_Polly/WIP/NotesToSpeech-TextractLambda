#This is a proof of concept with a few TODOs
#TODO - replace hard coded values
#TODY - create seperate function for multi-page documents
    #TODO - Seperate polly action into a seperate lambda function

import boto3, json, random
from io import BytesIO

#bucket and item name
bucket = 'serverless-app-bucket-nathan56765'
document = 'Bond-note_jpzejq.png'

# Service connection variables

# S3
s3_client = boto3.client("s3")
s3_connection = boto3.resource('s3')              
s3_object = s3_connection.Object(bucket,document)
s3_response = s3_object.get()

# Textract Client
client = boto3.client('textract')

# Dynamo DB Client
dynamodb = boto3.client('dynamodb')

# Polly Client
polly = boto3.client("polly")

def lambda_handler(event, context):
    
    # Event dump for notes
    print("Received event: " + json.dumps(event))
    
    # Final output string
    outStr = ""
    
    # Textract detect
    response = client.detect_document_text(Document={'S3Object': {'Bucket': bucket, 'Name': document}})
    # Output response to CloudWatch
    print(response)
    
    # Parse JSON response from Textract
    for item in response['Blocks']:
        if item['BlockType'] != 'LINE':
            continue
        else:
            print(item['Text'])
            outStr += item['Text'] + "\n"
        
    print(outStr)
    
    # Write outStr to DBB
    dynamodb.put_item(
        TableName='TextToSpeechDB',
        Item={
            'ID': {"S": str(random.randrange(1000))},
            'Text':{"S":  outStr}
        }
    )
        
    # Process text with Polly
    response = polly.synthesize_speech(
        Engine= 'neural',
        LanguageCode= 'en-US',
        OutputFormat='mp3',
        Text=outStr,
        TextType='text',
        VoiceId='Brian'
    )
    print(response)
    
    # Convert AudioStream 
    audiofile = response['AudioStream'].read()
    
    # Store Polly file in s3
    s3_client.put_object(Bucket=bucket, Key="TextToSpeech.mp3", Body=audiofile)
