# Client option

import boto3
client = boto3.client('s3')

response = client.create_bucket(
    Bucket='chamakebucket',
   
)

print(response)

# Resource option

import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("chamake2bucket")

response = bucket.create(
    ACL='public-read'
    
)

print(response)