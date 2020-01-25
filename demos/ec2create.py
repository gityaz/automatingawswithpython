import boto3
ec2 = boto3.resource('ec2')

def create_instance():
    ec2.create_instances(
        ImageId='ami-02ccb28830b645a41',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro')

create_instance()