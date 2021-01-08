https://www.wellarchitectedlabs.com/security/

# 200 Level

## REMOTE CONFIGURATION, INSTALLATION, AND VIEWING OF CLOUDWATCH LOGS

![](https://www.wellarchitectedlabs.com/Security/200_Remote_Configuration_Installation_and_Viewing_CloudWatch_Logs/Images/datadistancingarch.png)

### Key Takeaways

* Can use the Run Command in SSM to install the Cloudwatch Agent to your fleet at once - pretty useful
* Parameter store can be used for standardized configuration files
* CloudWatch logs can be exported to S3
  * Use Athena to query those logs 

### Lab Notes

* Launch CF stack with components
* Install CloudWatch Agent using the Run Command option in SSM
  * ![](https://www.wellarchitectedlabs.com/Security/200_Remote_Configuration_Installation_and_Viewing_CloudWatch_Logs/Images/install-cw-agent-3.png)
* Create a standard CloudWatch configuration file for our agent
* Use Parameter store to save the configuration file and make it available for our instances
* Using Run Command again, run "AmazonCloudWatch-ManageAgent" with our config file selected for "Option Configuration Location"
* Generate some logs by accessing the webpage
* View in Cloudwatch
* Export to S3
* Use Athena to query exported logs

## Basic EC2 WAF Protection

Supplemented materials with this YouTube video on WAFs - https://www.youtube.com/watch?v=p8CQcF_9280

### Key Takeaways

* Web application firewalls (WAF) monitors HTTP traffic in front of your ALB/API/GraphQL API
* A network firewall may stop attacks at the lower layers of your network (3/4)
  * ex. DDOS attack
* A WAF can detect attacks at the higher layers, (4/5-7)
 * ex. Slow loris - flood of legitimate, valid HTTP requests to saturate your network
 * these attacks are about attacking the application itself, not the network


## AWS Certificate Manager - Request Public Certificate

* Short lab 
* Good to know that AWS offers this service - providing Public Certificates for your owned domains

## CloudFront for Web Application


# 100 Level

## Account Settings and Root User Security

### Key Takeaways

* Disable User Access Keys on your Root account
* IAM console offers a Credentials Report
  * When were passwords/keys last cycled or used
