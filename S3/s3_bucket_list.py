# Resource option

import boto3
resource=boto3.resource("s3")

# Option 1

# response = list(resource.buckets.all())

# print(response)

# Option 2

#for buckets in resource.buckets.all():
    
#   print(buckets)

# Option 3 (to get only names)

#for buckets in resource.buckets.all():
    
#    print(buckets.name)
    
# Option 4 (no of buckets)

response = list(resource.buckets.all())

print(len(response))
