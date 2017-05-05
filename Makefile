publicIP=$(shell terraform output | awk '/publicIP/ {print $$3}' )

help:
	@printf 'Usage:\nRun "make prep" once to create the keys and groups.\nRun "make instance" to create the instance with Terraform.\nRun "make info" to get the IP addresses of the instance.\nRun "make deploy" to configure the instance with Ansible - give some to have a first boot.\nRun "make test" to test it all.\n(Other targets are destroy / unprep, ssh and uptime).\n'

prep:
	@-aws ec2 create-key-pair --key-name terraform --query 'KeyMaterial' --output text > terraform.pem
	@chmod 400 terraform.pem
	@-aws ec2 create-security-group --group-name terraform --description "Security group for Flask with Terraform";
	@-aws ec2 authorize-security-group-ingress --group-name terraform --protocol tcp --port 22 --cidr 0.0.0.0/0
	@-aws ec2 authorize-security-group-ingress --group-name terraform --protocol tcp --port 8000 --cidr 0.0.0.0/0

instance:
	@terraform plan
	@terraform apply

deploy:
	ansible-playbook -i $(publicIP), --user=ubuntu --private-key=terraform.pem --ssh-extra-args='-o StrictHostKeyChecking=no' playbook.yml

unprep destroy:
	@echo yes | terraform destroy
	@aws ec2 delete-security-group --group-name 'terraform' || true
	@aws ec2 delete-key-pair --key-name 'terraform' || true
	@rm -fv terraform.pem

#target to test ssh access to the instance
ssh:
	ssh -i terraform.pem -o StrictHostKeyChecking=no ubuntu@$(publicIP)

uptime:
	ssh -i terraform.pem -o StrictHostKeyChecking=no ubuntu@$(publicIP) uptime

nose:
	ssh -i terraform.pem -o StrictHostKeyChecking=no ubuntu@$(publicIP) 'nosetests /opt/fibonacci-api/test_resources.py'

test:
	curl -i -X GET "$(publicIP):8000/fibonacci/10"

info:
	@terraform output

