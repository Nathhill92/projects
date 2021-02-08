I am overhauling my WordPress project to include some more advanced features

Quick description

* Automate much of the environment with a CloudForamtion template
* Add Parameter Store / Secrets Manager to our configuration files
* Add Patch / Inventory Management to EC2 servers
* Add CodeDeploy to our EC2 servers
* Re-design EFS drive to only store Dynamic contents
* Enhanced monitoring with CloudWatch
* Add Serverless functionality to "disrupt" my environment to generate more scaling events
  * Delete / Stop Webserver
  * Simulate load
  * etc.

Documentation will come later

## Step 1 - Base Infrastructure

These components will not be deleted or created during the automated "start of day" and "end of day" operations. 

### Step 1a - VPC and Subnets

* CloudFormation Template

### Step 1b - Security Groups

* CloudFormation Template
 * Note about using CloudFormation to make Security Groups - If you need your SGs to reference eachother, do the Creation and Ingress separately. 
 
 ### step 1c - IAM Roles
 * Will automate this after doing it manually - to know exactly what permissions are needed
 
 ## Step 2 - Initial Component Creations
 
 * Initial creation is manual. This will be automated later using "restore from backup" options in CloudFormation.
 
 ### Step 2a - RDS
 * Follow the steps outlined here - https://aws.amazon.com/getting-started/hands-on/deploy-wordpress-with-amazon-rds/
 * Note - create the "WordPress" database at RDS instance creation time
   * Avoids permissions oddities - RDS "root" accounts have less access than typical database "root" accounts
 
 ### Step 2b - Elasticache
 
 ### Step 2c - EFS
 
 ## Step 3 - Webserver setup and AMI creation
 
 * Follow the steps outlined here - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hosting-wordpress.html
