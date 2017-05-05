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
The script is driven by make, in order to provide consistent user/ops experience. It seems that Terraform, in the current version, does not support creating keys for AWS, so some interaction with awscli would have been required anyways.

The instance config is done with Ansible. Migrating this part to the Chef provisioner would probably make more sense down the road.

Usage:

`git clone git@github.com:eyablokov/fibonacci-api.git`

`cd fibonacci-api`

Create a file called `terraform.tfvars` - this file is excluded from the repo in `.gitignore`. 
The file should have the AWS credentials in a format:

`access_key = "abc"`

`secret_key = "xyz"`



`make`          (this will print the help page)

`make prep`     (create the keys and security group with awscli)

`make instance` (the heavy lifting is done by terraform here, the terraform output will be the IP addresses of the instance)

`make info`     (shortcut for terraform output)

`make deploy`   (run the ansible playbook)
`make test`     (testing the service with curl)

`make nose`     (testing with [nose](http://nose.readthedocs.io))

`make destroy`  (terraform destroy && awscli delete keys and groups)
