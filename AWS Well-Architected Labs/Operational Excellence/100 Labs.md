## Inventory and Patch Management Lab Notes

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
