try:
    from aws_tool_box import ec2_tools
except ImportError:
    from aws_api_client.aws_tool_box import ec2_tools


def test_creating_and_deleting_ec2():
    test_instance_name = "delete_me_test"

    # Confirm there is no test_instance_name running
    assert not ec2_tools.find_running_ec2_by_name(test_instance_name)

    # Create ec2 instance
    ec2_id = ec2_tools.create_ubuntu_18_04(test_instance_name)

    # Wait for ec2 to be found
    ec2_found = ec2_tools.find_running_ec2_by_name(test_instance_name)

    while not ec2_found:
        ec2_found = ec2_tools.find_running_ec2_by_name(test_instance_name)

    # Confirm ec2 instance was created
    assert ec2_tools.find_running_ec2_by_name(test_instance_name)

    # Delete ec2 instance
    ec2_tools.delete_instances(ec2_id)

    # Confirm ec2 was deleted
    assert not ec2_tools.find_running_ec2_by_name(test_instance_name)





