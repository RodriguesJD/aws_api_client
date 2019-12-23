from aws_tool_box import ec2_tools


def test_get_all_instances():
    instances = ec2_tools.get_all_running_ec2()
    assert isinstance(instances, list)
    for instance in instances:
        assert isinstance(instance, dict)


def test_find_ec2_by_name():
    for instance in ec2_tools.get_all_running_ec2():
        instance_name = instance['Tags'][0]['Value']
        assert isinstance(instance_name, str)
        lookup_name = ec2_tools.find_running_ec2_by_name(instance_name)
        assert lookup_name
        assert isinstance(lookup_name, dict)

    not_ec2 = "this is not an ec2 name"
    assert not ec2_tools.find_running_ec2_by_name(not_ec2)
