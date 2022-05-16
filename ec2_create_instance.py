# Importing boto3 library to make functionality available
 import boto3
# Creating the connection with the resource of AWS EC2 service
 ec2 = boto3.resource('ec2')
# creating a new EC2 instance
 instances = ec2.create_instances(
      ImageId='ami-09d56f8956ab235b3',
      MinCount=1,
      MaxCount=1,
      InstanceType='t2.micro',
  )
  print("AWS EC2 Instance Launched successfully")
