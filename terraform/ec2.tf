resource "aws_instance" "bastion" {
  ami = "ami-019715e0d74f695be"
  instance_type = "t3.micro"
  subnet_id = module.vpc.public_subnets[0]
}
