import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-09d3b3274b6c5d4aa',
        InstanceType='t1.micro',
    MaxCount=1,
        MinCount=1)