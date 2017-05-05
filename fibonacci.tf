provider "aws" {
    access_key = "${var.access_key}"
    secret_key = "${var.secret_key}"
    region = "${var.region}"
}

resource "aws_instance" "fibonacci" {
    ami = "ami-9abea4fb"
    instance_type = "t2.micro"
    key_name = "terraform"
    security_groups = ["terraform"]
}

output "publicIP" {
    value = "${aws_instance.fibonacci.public_ip}"
}

output "privateIP" {
    value = "${aws_instance.fibonacci.private_ip}"
}
