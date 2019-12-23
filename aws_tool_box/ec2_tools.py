import os
from pprint import pprint

import boto3

key_name = os.environ["AWS_PEM_KEY"]
image_id = os.environ["AWS_IMAGE_ID"]

ec2 = boto3.resource('ec2')


def create_ubuntu_18_04(name):
    instances = ec2.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName=key_name,
        TagSpecifications=[{'ResourceType': 'instance', 'Tags': [{'Key': 'Name', 'Value': name}]}]
    )
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance.id)

    return instance_ids


def delete_instances(instance_ids):
    ec2.instances.filter(InstanceIds=instance_ids).terminate()


def get_all_running_ec2():
    instances = []
    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if instance["State"]["Name"] == "running":
                instances.append(instance)

    return instances


def find_running_ec2_by_name(ec2_name):
    test_instance_found = False
    for instance in get_all_running_ec2():
        instance_name = instance['Tags'][0]['Value']
        if instance_name == ec2_name and instance["State"]["Name"] == "running":
            test_instance_found = instance

    return test_instance_found

# TODO create a functional test that creates, then terminate an instance.


