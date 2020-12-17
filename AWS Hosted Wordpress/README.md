<a href="https://i.imgur.com/xXAsXWm.png" imageanchor="1"><img src="https://i.imgur.com/xXAsXWm.png" border="0"></a>

<b>Summary</b>

This project represents a scalable WordPress website utilizing IaaS and PaaS AWS services.
Every component of this application was built personally without any existing automation templates. Including the VPC, Subnets, Security Groups, IAM users/roles, and application components.
This project was inspired by the AWS Well-Architected Framework and AWS's Best Practices for WordPress.

<b>Components</b>

<b>Application/Web Tier</b>

•	The WordPress site is hosted on a fleet of Autoscaling EC2 instances across two Availability Zones

•	Static site content (media) is delivered through an S3 bucket 

•	Both the static and dynamic content are delivered through CloudFront to accelerate site load times

<b>Data Tier</b>

•	The data tier makes use of PaaS solutions offered by AWS.

•	Web server contents are delivered with EFS, allowing for low-latency, concurrent, and persistent data

•	The application database uses RDS with MariaDB.

o	A Primary database is maintained for write operations

o	A Read Replica is used for read-only operations

•	An Elasticache node is used to cache database queries for the site contents with Memcached

<b>Future Considerations</b>

•	Lock down SSH access to the web server with a Bastion Host

•	Purchase and use a domain name through Route53

•	Switch database solution to Amazon Aurora to add better scaling capabilities

•	Operate the site as a serverless solution with Fargate or Elastic Beanstalk  

<b>Lessons Learned</b>

•	PHP webservers run very poorly without byte caching enabled, especially across AZs

•	EFS adds a trivial amount of latency in this context - https://aws.amazon.com/blogs/startups/how-to-accelerate-your-wordpress-site-with-amazon-cloudfront/

•	PHP-fpm runs as the “apache” user by default, change to match with your web server user account - nginx in my case

•	By default, WordPress generates its hyperlinks from a DB entry. This is an IP address, which doesn't really work in an elastic context. Make sure to change to the url for your ELB.
