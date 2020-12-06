# template source - https://gist.githubusercontent.com/BetterProgramming/a62909208e9f6cbd0319765695ee065d/raw/cb7e3ce1a19e18e56425ee6a3a3d369e67bcec1c/RawTextImageExtract.py
# Article for Textract Piece - https://medium.com/better-programming/extract-data-from-pdf-files-using-aws-textract-with-python-12ba62fde1b0

import boto3
import time

def startJob(s3BucketName, objectName):
    response = None
    client = boto3.client('textract')
    response = client.start_document_text_detection(
        DocumentLocation={
            'S3Object': {
            'Bucket': s3BucketName,
            'Name': objectName
            }
        }
    )
    return response["JobId"]


def isJobComplete(jobId):
 # For production use cases, use SNS based notification 
 # Details at: https://docs.aws.amazon.com/textract/latest/dg/api-async.html
 time.sleep(5)
 client = boto3.client('textract')
 response = client.get_document_text_detection(JobId=jobId)
 status = response["JobStatus"]
 print("Job status: {}".format(status))
while(status == "IN_PROGRESS"):
 time.sleep(5)
 response = client.get_document_text_detection(JobId=jobId)
 status = response["JobStatus"]
 print("Job status: {}".format(status))
return status


def getJobResults(jobId):
pages = []
client = boto3.client('textract')
 response = client.get_document_text_detection(JobId=jobId)
 
 pages.append(response)
 print("Resultset page recieved: {}".format(len(pages)))
 nextToken = None
 if('NextToken' in response):
 nextToken = response['NextToken']
while(nextToken):
response = client.get_document_text_detection(JobId=jobId, NextToken=nextToken)
pages.append(response)
 print("Resultset page recieved: {}".format(len(pages)))
 nextToken = None
 if('NextToken' in response):
 nextToken = response['NextToken']
return pages
# Document
s3BucketName = "<Your S3 Bucket name>"
documentName = "<Path to the PDF inside the bucket>"
jobId = startJob(s3BucketName, documentName)
print("Started job with id: {}".format(jobId))
if(isJobComplete(jobId)):
 response = getJobResults(jobId)
#print(response)
# Print detected text
for resultPage in response:
 for item in resultPage["Blocks"]:
 if item["BlockType"] == "LINE":
 print ('\033[94m' + item["Text"] + '\033[0m')