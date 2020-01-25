# List Objects in Bucket using the Client API 
# Return type: dict / additional API calls needed to get objects

import boto3

s3client = boto3.client('s3')
response = s3client.list_objects_v2(Bucket='lambdas3fun')
for content in response['Contents']:
    print(content['Key'],content['LastModified'])



