import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_snapshot(Description='Snapshot from base volume using python',
                          VolumeId='vol-06694c7aabcf60963')
