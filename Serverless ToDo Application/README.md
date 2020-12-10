<img src="https://i.imgur.com/WYfn9ly.png" border="0">

<b>Summary</b>

This application is acts as a Daily “To Do” List with email reminders. 


<b>Components and Application Flow</b>
1.	Static S3 Website - users enter task data and due time
2.	API Gateway accepts the Submit request (POST) and forwards user data to Lambda
3.	Lambda Function #1 - Validates task data and stores the data in - 
4.	DynamoDB 
5.	EventBridge - uses CloudWatch Events to invoke Lambda once per hour
6.	Lambda Function #2 - Scans DynamoDB for tasks coming due and sends an email reminder to - 
7.	Simple Email Service
8.	IAM Roles allowing AWS services to access each other (Lambda, DynamoDB, CloudWatch, SES)


<b>Future Considerations</b>

•	Create a new EventBridge/Lambda function to purge old tasks

•	Move the static S3 Website into Amplify to allow for easier code change deployments

<b>Inspired</b> by AWS Serverless Workshops and ACantrill's labs on Reddit

1. https://github.com/aws-samples/aws-serverless-workshops
2. https://www.reddit.com/r/AWSCertifications/comments/jh42w0/free_weekend_aws_demo_challenge/