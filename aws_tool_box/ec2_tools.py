import os
from pprint import pprint

import boto3

key_name = os.environ["AWS_PEM_KEY"]
image_id = os.environ["AWS_IMAGE_ID"]


def ec2_print_all():
    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        pprint(reservation)


def create_ubuntu_18_04(name):
    ec2 = boto3.resource('ec2')
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
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=instance_ids).terminate()
