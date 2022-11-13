import boto3

ec2_resource=boto3.resource('ec2')

# Find all running instances with Dev tag

instances = ec2_resource.instances.filter(
    Filters = [{'Name': 'instance-state-name', 'Values': ['running']},
    {'Name':'tag:Environment','Values':['Dev']}]
)

for instance in instances:
    try:
        instance.stop()
        print(f'{instance} stopped')
        
    except:
        print(f'Error stopping {instance}')