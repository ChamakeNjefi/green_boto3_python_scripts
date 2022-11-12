import boto3
ec2_client=boto3.client("ec2")

x=ec2_client.describe_instances()
data=x["Reservations"]

for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        print(instance_id)
        
ec2_client.terminate_instances(InstanceIds=['i-08e3824984b65322a', 'i-047972695ca79f825', 'i-01495d4e9ae7928f7', 'i-05d28cd3d55faa1be'
           ])

