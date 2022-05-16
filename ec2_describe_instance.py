# Importing boto3 library to make functionality available
import boto3
# Creating a client connection with AWS EC2 
ec2 = boto3.client('ec2')
# Using the Describe_Instance Method along with filters
instance = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': ['KCDCHENNAI-DEMO']}])
print(instance)
