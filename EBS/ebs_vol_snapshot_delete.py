import boto3
ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='snap-02ecfd7d01474376b')
