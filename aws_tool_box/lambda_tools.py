import os
import boto3
from pprint import pprint


profile_name = os.environ["AWS_DEV_PROFILE"]

lambda_resource = boto3.session.Session(profile_name=profile_name, region_name="us-west-1").client('lambda')


def find_lambda_function(function_name):
    return lambda_resource.get_function(FunctionName=function_name)


def find_all_lambda_functions_in_region():
    return lambda_resource.list_functions()


def create_lambda_function():
    create = lambda_resource.create_function(
        FunctionName="boto3_create_func",
        Runtime='python3.8',
        Role='arn:aws:iam::725960340569:role/service-role/it_testing',
        Handler='lambda_function.lambda_handler',
        Code={
            'ZipFile': open("/Users/jrodrigues/lambda_function.py.zip", 'rb').read()
        },
        Description='boto3 func des test',
        Timeout=3,
        MemorySize=128,
        Publish=True
    )
    print(create)
