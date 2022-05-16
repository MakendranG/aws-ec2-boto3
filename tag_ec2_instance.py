# Importing boto3 library to make functionality available
import boto3
# Creating the connection with the resource of AWS EC2 service 
ec2 = boto3.resource('ec2')
# Adding the Tag KCDCHENNAI-DEMO for AWS EC2 using the instance ID
response = ec2.create_tags(
    Resources=[
        '#### ENTER THE INSTANCE ID ###',      
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'KCDCHENNAI-DEMO'
        },
    ]
)
