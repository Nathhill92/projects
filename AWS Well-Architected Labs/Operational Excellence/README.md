## Inventory and Patch Management Lab Notes

### Key Takeaways

* Use tags and resource groups to adminster fleets of servers with SSM
* set patching baselines to automate patching process
* use "Run Command" in SSM to administer commands to many servers at once

### SSM Notes
* AWS Systems Manager is used to administer fleets of servers - normally defined by tags or resource group
* SSM is combatible with *Windows, Amazon Linux AMIs, Ubuntu Server, RHEL, and CentOS*
* For SSM to function, your servers need to have an attached IAM role with permissions to SSM
  * "AmazonEC2RolefoSSM" used for this lab
  * *least privileges* guideline - https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-iam-user.html 
 
### Lab Notes
* Create test and prod environments with given CloudFormation template
* Attach IAM role with access to SSM
* Create an inventory association using the instance tag "Environment:OELabIPM"
* Under Patch Baseline, Create a policy defining when and how to apply updates to our instance fleet
  * For our dashboard, patches with security updates are marked as "critical" and "moderate" for patches without security updates
* Under "Run Command", run the AWS-RunPatchBaseLine
  * For targets, specify the tag "Workload:test"
  * All of our test servers have been patched 
  
![test servers patched](https://i.imgur.com/uUeqgHL.png)

* Create a Maintenance Window to apply patches during business downtime/off hours
  * Offers advanced options for reporting, stop times, tracking error percentages

## Dependency Monitoring Lab Notes

### Key Takeaways

* Combining OpsItems and CloudFormation can help organize the efforts around triaging/troubleshooting environment issues
 * "AWS console" way of doing incident management

### Lab Notes

* Create environemnt with given CloudFormation template
* Create an alarm that - Specified Lambda executes at least once per minute
* Create a fail condition on purpose - delete the IGW from our routing table
 * This disallows our app to write to S3, triggering the alarm
 * Receive failure email through SNS
 
* Bonus step - Create an OpsItem to provide more details on the failure
 * Attacch a Lambda function to the existing SNS topic that creates the OpsItem 
