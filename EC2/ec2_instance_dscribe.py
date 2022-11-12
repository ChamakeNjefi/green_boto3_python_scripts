import boto3

ec2_client=boto3.client('ec2')
x=ec2_client.describe_instances()

no_of_instances=x["Reservations"]

# To get full description of all instances

for instance in no_of_instances:
   print(instance)


# To get # of instances & Instance ID

#print(len(no_of_instances))

#for r in x['Reservations']:
 #   for i in r['Instances']:
  #      print (i['InstanceId'])




