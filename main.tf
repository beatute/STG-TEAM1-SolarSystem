provider "aws" {
  region = var.region
}

resource "aws_key_pair" "team1_key_pair" {
  key_name   = var.key_name
  public_key = file(var.public_key_path)
}

resource "aws_security_group" "team1_security_group" {
  name        = var.security_group_name

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "team1_solar_system" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = aws_key_pair.team1_key_pair.key_name
  tags          = {
    Name = "team1_solar_system"
  }
  vpc_security_group_ids = [aws_security_group.team1_security_group.id]


  provisioner "local-exec" {
  command = "sleep 60 && ansible-playbook -i '${aws_instance.team1_solar_system.public_ip},' -e ip_address=${aws_instance.team1_solar_system.public_ip} final_playbook.yml --user ${var.aws_instance_user_id} --private-key ${var.private_key_path}"
}
}
