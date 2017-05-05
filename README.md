fibonacci-api
=============

The REST API for generating [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence).

Using this repository, you'll deploy Flask REST API application on AWS, with Terraform, Ansible and Makefile.


Dependencies:
- bash 4+;
- fully configured aws cli, tested with the AWS free tier;
- Ansible 2+;
- Terraform v0.6+;
- make or gmake.

Tested on Ubuntu 17.04 with default repos.

Description:
  The script is driven by make, in order to provide consistent user/ops experience. It seems that terraform in the current version does not support creating keys for AWS, so some interaction with awscli would have been required anyways.

The instance config is done with ansible, by reusing the code in the master branch. Migrating this part to the chef provisoner would probably make more sense down the road.

Usage:
  git clone git@github.com:marikgoran/hello-aws.git
  cd hello-aws
  git checkout terraform
  # create a file called terraform.tfvars - this file is excluded from the repo in .gitignore. 
  # the file should have the AWS credentials in a format:
  # access_key = "abc"
  # secret_key = "xyz"
  ## 
  make            ( this will print the help page ) 
  # 
  make prep       ( create the keys and security group with awscli )
  make instance   ( the heavy lifting is done by terraform here, the terraform output will be the IP addresses of the instance)
  make info       ( shortcut for terraform output )
  make deploy     ( run the ansible playbook ) 
  make hello      ( testing the service with curl)
  make destroy    ( terraform destroy && awscli delete keys and groups )
