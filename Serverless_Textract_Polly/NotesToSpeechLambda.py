import boto3, json, random
from io import BytesIO

# bucket and item name
bucket = 'serverless-app-bucket-nathan56765'
# hard written value for testing
document = 'Bond-note_jpzejq.png'

# Service connection variables

# S3
s3_connection = boto3.resource('s3')              
s3_object = s3_connection.Object(bucket,document)
s3_response = s3_object.get()

# Textract
client = boto3.client('textract')

# Dynamo DB Client
dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
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
    
    #return code
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
