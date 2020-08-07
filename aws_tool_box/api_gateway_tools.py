import boto3
import os

profile_name = os.environ["AWS_DEV_PROFILE"]

api_gateway_resource = boto3.session.Session(profile_name=profile_name, region_name="us-west-1").client('apigateway')


def find_all_rest_api_gateways():
    return api_gateway_resource.get_rest_apis()


def find_all_resources(rest_api_id):
    return api_gateway_resource.get_resources(restApiId=rest_api_id)


def create_rest_api_gateway():
    api_gateway_resource.create_rest_api(
        name='boto3_made_gateway',
        description='create api gateway with boto3',
        apiKeySource='HEADER',
        endpointConfiguration={
            'types': [
                'REGIONAL'
            ]
        }
    )


def create_api_resource(rest_api_id):
    api_gateway_resource.create_resource(
        restApiId=rest_api_id,
        parentId='6jppab18wj',
        pathPart='/'
    )
