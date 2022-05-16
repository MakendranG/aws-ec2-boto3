import boto3
# Creating a client connection with AWS EC2 
ec2 = boto3.client('ec2')
# Use response = ec2.start_instances( if you need to Start the Machine)
# Use response = ec2.terminate_instances( if you need to terminate the Machine)

# Stopping the instance using stop_instances.
response = ec2.stop_instances(
	    InstanceIds=[
        '### INSTANCE ID ###',
    ],
)
