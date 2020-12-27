![alt text](https://i.imgur.com/WYfn9ly.png)

# <b>Summary</b>

This application is acts as a Daily “To Do” List with email reminders. 


# <b>Components and Application Flow</b>
1.	<b>Static S3 Website</b> - users enter task data and due time
2.	<b>API Gateway</b> accepts POST request and forwards user data to Lambda
3.	<b>Lambda</b> Function #1 - Validates task data and stores the data in - 
4.	<b>DynamoDB</b> 
5.	<b>EventBridge</b> - uses CloudWatch Events to invoke Lambda once per hour
6.	<b>Lambda</b> Function #2 - Scans DynamoDB for tasks coming due and sends an email reminder to - 
7.	<b>SES</b> - Simple Email Service
8.	<b>IAM</b> Roles allowing AWS services to access each other (Lambda, DynamoDB, CloudWatch, SES)


# <b>Future Considerations</b>

•	Create a new EventBridge/Lambda function to purge old tasks

•	Move the static S3 Website into Amplify to allow for easier code change deployments

•	AWS account is in "sandbox" mode and cannot send SMS/Email messages. For the purpose of these home labs, only being able to email myself is fine.

<b>Inspired</b> by AWS Serverless Workshops and ACantrill's labs on Reddit

1. https://github.com/aws-samples/aws-serverless-workshops
2. https://www.reddit.com/r/AWSCertifications/comments/jh42w0/free_weekend_aws_demo_challenge/

## Web page Image -

![alt text](https://i.imgur.com/7nKu681.png)
