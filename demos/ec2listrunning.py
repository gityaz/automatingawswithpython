# Boto 3
# Use the filter() method of the instances collection to retrieve
# all running EC2 instances.

import boto3

ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)