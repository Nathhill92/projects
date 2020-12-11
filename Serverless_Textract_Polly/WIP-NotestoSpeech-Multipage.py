import boto3, json, sys, time

#Env Variables
jobId = ''
textract = boto3.client('textract')
sqs = boto3.client('sqs')
sns = boto3.client('sns')

roleArn = 'arn:aws:iam::630407588899:role/TextractRole'  
sqsQueueUrl = 'arn:aws:sqs:us-east-1:630407588899:NotesToSpeech-Textract-SQS'
snsTopicArn = 'arn:aws:sns:us-east-1:630407588899:NotesToSpeech-Textract-SNS'

# Feed Doc to Textract
def ProcessDocument(bucket, document):
    jobFound = False

    # Textract page start
    response = textract.start_document_text_detection(DocumentLocation={'S3Object': {'Bucket': bucket, 'Name': document}},
        NotificationChannel={'RoleArn': roleArn, 'SNSTopicArn': snsTopicArn})

    print('Start Job Id: ' + response['JobId'])
        
    dotLine=0
    while jobFound == False:
        sqsResponse = sqs.receive_message(QueueUrl=sqsQueueUrl, MessageAttributeNames=['ALL'],
                                        MaxNumberOfMessages=10)

        if sqsResponse:
            
            if 'Messages' not in sqsResponse:
                if dotLine<40:
                    print('.', end='')
                    dotLine=dotLine+1
                else:
                    print()
                    dotLine=0    
                sys.stdout.flush()
                time.sleep(5)
                continue

            for message in sqsResponse['Messages']:
                notification = json.loads(message['Body'])
                textMessage = json.loads(notification['Message'])
                print(textMessage['JobId'])
                print(textMessage['Status'])
                if str(textMessage['JobId']) == response['JobId']:
                    print('Matching Job Found:' + textMessage['JobId'])
                    jobFound = True
                    GetResults(textMessage['JobId'])
                    sqs.delete_message(QueueUrl=sqsQueueUrl,
                                    ReceiptHandle=message['ReceiptHandle'])
                else:
                    print("Job didn't match:" +
                            str(textMessage['JobId']) + ' : ' + str(response['JobId']))
                # Delete the unknown message. Consider sending to dead letter queue
                sqs.delete_message(QueueUrl=sqsQueueUrl,
                                ReceiptHandle=message['ReceiptHandle'])

        print('Done!')

# Block Info
def DisplayBlockInfo(block):
    
    print ("Block Id: " + block['Id'])
    print ("Type: " + block['BlockType'])
    if 'EntityTypes' in block:
        print('EntityTypes: {}'.format(block['EntityTypes']))

    if 'Text' in block:
        print("Text: " + block['Text'])

    if block['BlockType'] != 'PAGE':
        print("Confidence: " + "{:.2f}".format(block['Confidence']) + "%")

    print('Page: {}'.format(block['Page']))

    if block['BlockType'] == 'CELL':
        print('Cell Information')
        print('\tColumn: {} '.format(block['ColumnIndex']))
        print('\tRow: {}'.format(block['RowIndex']))
        print('\tColumn span: {} '.format(block['ColumnSpan']))
        print('\tRow span: {}'.format(block['RowSpan']))

        if 'Relationships' in block:
            print('\tRelationships: {}'.format(block['Relationships']))

    print('Geometry')
    print('\tBounding Box: {}'.format(block['Geometry']['BoundingBox']))
    print('\tPolygon: {}'.format(block['Geometry']['Polygon']))
    
    if block['BlockType'] == 'SELECTION_ELEMENT':
        print('    Selection element detected: ', end='')
        if block['SelectionStatus'] =='SELECTED':
            print('Selected')
        else:
            print('Not selected')  

# Get Results
def GetResults(jobId):
    maxResults = 1000
    paginationToken = None
    finished = False

    while finished == False:

        response=None
    
        if paginationToken==None:
            response = textract.get_document_analysis(JobId=jobId,
                MaxResults=maxResults)
        else: 
            response = textract.get_document_analysis(JobId=jobId,
                MaxResults=maxResults,
                NextToken=paginationToken)                           

        blocks=response['Blocks'] 
        print ('Detected Document Text')
        print ('Pages: {}'.format(response['DocumentMetadata']['Pages']))
    
        # Display block information
        for block in blocks:
                DisplayBlockInfo(block)
                print()
                print()

        if 'NextToken' in response:
            paginationToken = response['NextToken']
        else:
            finished = True

# Lambda Handler / "Main"
def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        document = record['s3']['object']['key']

    print(bucket)
    print(document)
    #ProcessDocument(bucket, document)

    #return code
