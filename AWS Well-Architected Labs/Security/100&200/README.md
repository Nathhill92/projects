https://www.wellarchitectedlabs.com/security/
  
# 200 Level

## Basic EC2 WAF Protection

Supplemented materials with this YouTube video on WAFs - https://www.youtube.com/watch?v=p8CQcF_9280

### Key Takeaways

* Web application firewalls (WAF) monitors HTTP traffic in front of your ALB/API/GraphQL API
* A network firewall may stop attacks at the lower layers of your network (3/4)
  * ex. DDOS attack
* A WAF can detect attacks at the higher layers, (4/5-7)
 * ex. Slow loris - flood of legitimate, valid HTTP requests to saturate your network
 * these attacks are about attacking the application itself, not the network



# 100 Level

## Account Settings and Root User Security

### Key Takeaways

* Disable User Access Keys on your Root account
* IAM console offers a Credentials Report
  * When were passwords/keys last cycled or used
