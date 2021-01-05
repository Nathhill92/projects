![alt text](https://i.imgur.com/4ddJFL8.png)

## <b>Summary</b>

This application accepts images of notes, handwritten or typed, and used Textract and Polly to turn those notes into an MP3 audio file.


## <b>Components and Application Flow</b>

1.	<b>S3</b> Bucket stores user uploaded JPG/PNG/PDF and also the final MP3
2. <b>Lambda</b> Function processes the input file and directs it to the next stage based on it's file extension. JGP/PNG/PDF files are forwarded for further processing, while MP3 file trigger code to notify the user that Polly has completed.
3. <b>SNS/SQS Fanout Queue</b> forward the files to their correct functions for processing.
4. <b>Lambda</b> functions for the seperate PDF and Image file processes
5. <b>Textract Process</b> this represents the components Textract uses to process PDF documents
6. <b>DynamoDB</b> stores text output from Textract, as well as Metadata about that text
7. <b>Lambda</b> function to forward this text to Polly
8. <b>Polly</b> Converts stored text to an .MP3 audio file
9. <b>(Undocumented) CloudFormation</b> stores logs and errors in application flow


## <b>Lessons Learned</b>

1. The subscription filter feature in SNS uses the Message Attributes (metadata) fields, not the passed data field
2. To pass JSON objects between SNS and SQS, select "Enable Raw Message Delivery" in the SNS queue
3. PDF files, particularly large ones, require a seperate, asynchronous Textract process. This requires a specific SNS topic, SQS queue, and IAM role allowing these services to communicate.
4. Online JSON parsers make the incredibly long Textract respones much more readable - https://jsonformatter.curiousconcept.com/# - also useful for parsing "event" data in Lambda
5. SES requires that your account be out of "Sandbox" mode to send SMS and email messages from AWS
6. Use Versioning in Lambda to keep track of iterations - make sure that your connected services are configured to use only the "$LATEST" tag (if appropriate) as to not double process

### <b>Inspired</b> by AWS Serverless Workshops and ACantrill's labs on Reddit

1. https://github.com/aws-samples/aws-serverless-workshops
2. https://www.reddit.com/r/AWSCertifications/comments/jh42w0/free_weekend_aws_demo_challenge/
