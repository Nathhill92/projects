#!/bin/bash
#Install Packages
yum update -y
yum install httpd
amazon-linux-extras install -y php7.2

#Install WordPress
mkdir /var/www
cd /var/www
wget http://wordpress.org/latest.tar.gz
tar xzvf latest.tar.gz
cd /var/www/wordpress
cp wp-config-sample.php wp-config.php

#Apache Config
systemctl start httpd
systemctl enable httpd
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www && find /var/www -type d -exec sudo chmod 2775 {} \;


#Other Considerations
yum install php-opcache
