import boto3

ec2_resource=boto3.resource("ec2")

newinstance=ec2_resource.create_instances(
    ImageId='ami-09d3b3274b6c5d4aa',
    InstanceType='t2.micro',
    MaxCount=3,
    MinCount=3,
    TagSpecifications=[ 
                        
      {'ResourceType': 'instance',
       'Tags': [
           
           {'Key': 'Name', 
            'Value':'Prod-env'
            },
           
           {'Key': 'Environment', 
            'Value':'Prod'
           }
           ]
            }
   
        ]
    )
                           
for instanceId in newinstance:
    print("Prod-env instance id is:", instanceId)
      
                           
# Launching instances in Dev Environment                       
                           
    #TagSpecifications=[ 
                        
      #{'ResourceType': 'instance',
       #'Tags': [
           
        #   {'Key': 'Name', 
         #   'Value':'Dev-env'
          #  },
           
           #{'Key': 'Environment', 
            #'Value':'Dev'                         
                           
#for instanceId in newinstance:
#    print("Dev-env instance id is:", instanceId)                     
                           
                           