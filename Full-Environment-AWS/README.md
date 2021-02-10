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

* CloudFormation Template linked above
* Creates VPC and Subnets in us-east-1
* 1 Private and 1 Public subnet each across 3 availability zones

### Step 1b - Security Groups

* CloudFormation Template
  * Note about using CloudFormation to make Security Groups - If you need your SGs to reference eachother, do the Creation and Ingress separately.
* Webserver
  * Webserver SSH
* Load Balancer
* EFS
* Elasticache
* RDS
 
 ### step 1c - IAM Roles
 * Will automate this after doing it manually - to know exactly what permissions are needed
 
 ## Step 2 - Initial Component Creations
 
 * Initial creation is manual. This will be automated later using "restore from backup" options in CloudFormation.
 
 ### Step 2a - RDS
 * Follow the steps outlined here - https://aws.amazon.com/getting-started/hands-on/deploy-wordpress-with-amazon-rds/
 * Note - create the "WordPress" database at RDS instance creation time
   * Avoids permissions oddities - RDS "root" accounts have less access than typical database "root" accounts
 * Create a Read Replica - will mount this later in "WordPress Plugins" step
 
 ### Step 2b - Elasticache
 
 ### Step 2c - EFS
 * Make sure to attach new Security Groups allowing NFS access to your webserver
 * Attach EFS to /var/www (or whatever you set as your root directory)
 * Update the fstab file on your webserver following these instructions - https://docs.aws.amazon.com/efs/latest/ug/mount-fs-auto-mount-onreboot.html
 
 ## Step 3a - Webserver setup
 
* Follow the steps outlined here - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hosting-wordpress.html
* Install opcache and add the configuration changes listed here - https://aws.amazon.com/blogs/storage/optimizing-wordpress-performance-with-amazon-efs/
  * This will DRAMATICALLY speed up multiserver/EFS WordPress implementations by caching compiled PHP

## Step 3b - WordPress Plugins

## Step 3c - AMI Creation

## Step 3d - Elastic Load Balancer Creation and Target Registration

## Step 3e - Autoscaling Group Configuration


