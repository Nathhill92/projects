# handles png and jpg

import boto3, json, random

# Textract Client
client = boto3.client('textract')
# Dynamo DB Client
dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    
    # Event dump for notes
    print("Received event: " + json.dumps(event))
    for record in event['Records']:
        print("printing event output...")
        parsed_message = json.loads(record['body'])
        print(parsed_message)
        document = parsed_message['Data']['document']
        bucket = parsed_message['Data']['bucket']
    
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
            'FileName':{"S": document},
            'Bucket':{"S": bucket},
            'Text':{"S":  outStr},
        }
    )
   
    #return code
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
