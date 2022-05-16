# Importing boto3 library to make functionality available
import boto3
# Creating a client connection with AWS EC2 
ec2 = boto3.client('ec2')
# Using the Describe_Instance Method and filters to get a list of instances which are currently running
#.get("Reservations") is used when you need to work with more than one instance. As each instance gets a single reservation.
reservations = ec2_client.describe_instances(Filters=[
    {
        "Name": "instance-state-name",
        "Values": ["running"],
    }
]).get("Reservations")

# Using for loop() to iterate over reservations to generate instance id, instance type, and private IP address of running instances 
for reservation in reservations:
    for instance in reservation["Instances"]: ## Each reservation has an embedded Instances array that contains all EC2 instances in the reservation
        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]
        private_ip = instance["PrivateIpAddress"]
        public_ip = instance["PublicIpAddress"]
        print(f"{instance_id}, {instance_type}, {private_ip}, {public_ip}")
