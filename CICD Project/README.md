
# Summary

This project was apart of the Udemy course -  [DevOps Project: CI/CD with Jenkins Ansible Docker Kubernetes
](https://www.udemy.com/course/valaxy-devops/)

![alt-text](https://i.imgur.com/EFeAB9E.png "Project Diagram")

## <b>Application Flow</b>

- The application flow, depicted below, is as follows:
- A developer commits a code change to GitHub
- GitHub triggers a flag in our Jenkins server
- Jenkins activates a Maven build project to convert our Java code into a .war file
- Jenkins executes the following Playbooks on our Ansible server


<b>CI</b>

- Builds a Docker image based on the new *.war file 
- Pushes that Docker image to DockerHub with the "latest" tag

<b>CD</b>

- Deploys the new application to our Kubernetes cluster using a rolling deployment and liveness probes
- Deploys the image to our Kubernetes cluster


Original Documentation - https://docs.google.com/document/d/1guidLAypmySw5eGsrqBMfQlwZyjU25QU-qBB85i2nzI/edit
