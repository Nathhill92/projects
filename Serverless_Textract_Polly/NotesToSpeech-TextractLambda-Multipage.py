#handles PDF and multipage PDF documents

import boto3, json, sys, time, random

#Env Variables
outStr= ''
jobId = ''
textract = boto3.client('textract')
#sqs = boto3.client('sqs')
#sns = boto3.client('sns')
dynamodb = boto3.client('dynamodb')

#roleArn = 'arn:aws:iam::630407588899:role/TextractRole'  
roleArn = "arn:aws:iam::630407588899:role/Textract-Polly-LambdaRole"
sqsQueueUrl = 'https://sqs.us-east-1.amazonaws.com/630407588899/NotesToSpeech-Textract-SQS'
snsTopicArn = 'arn:aws:sns:us-east-1:630407588899:NotesToSpeech-Textract-SNS'

# Feed Doc to Textract
def ProcessDocument(bucket, document):
    jobFound = False

    # Textract page start
    response = textract.start_document_text_detection(DocumentLocation={'S3Object': {'Bucket': bucket, 'Name': document}},
        NotificationChannel={'RoleArn': roleArn, 'SNSTopicArn': snsTopicArn})

    print('Start Job Id: ' + response['JobId'])
    
    # Poll SNS for updates/completion
    isFinished = False
    while not isFinished:
        snsResponse = textract.get_document_text_detection(
            JobId=response['JobId'],
        )
        
        if snsResponse['JobStatus'] == "IN_PROGRESS":
            print("In Progress...")
            time.sleep(5)
            continue
        else:
            isFinished = True
            print("Finished")
            print(snsResponse)
            response_parser(snsResponse, bucket, document)

# Parse response into a string and place into DynamoDB          
def response_parser(snsResponse, bucket, document):
    outStr = ""
    # Parse response into string object
    for item in snsResponse['Blocks']:
        if item['BlockType'] != 'LINE':
               continue
        else:
            print(item['Text'])
            outStr += item['Text'] + " "
    
    # Write output to DynamoDB        
    if len(outStr) > 1:
        dynamodb.put_item(
            TableName='TextToSpeechDB',
            Item={
                'ID': {"S": str(random.randrange(1000,10000))},
                'FileName':{"S": document},
                'Bucket':{"S": bucket},
                'Text':{"S":  outStr}
            }
        )
                
# Lambda Handler / "Main"
def lambda_handler(event, context):
    
    # output event
    print(event)
    
    # parse event for doc and bucket
    message = event['Records'][0]['body']
    parsed_message = json.loads(message)
    bucket = parsed_message['Data']['bucket']
    document = parsed_message['Data']['document']
    print('Bucket and Document values...')
    print(bucket)
    print(document)
    
    print('Starting Process Document...')
    ProcessDocument(bucket, document)
