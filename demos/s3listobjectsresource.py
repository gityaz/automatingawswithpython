# List Objects in Bucket using the Resource API
# Resources represent an object-oriented interface to Amazon Web Services (AWS). They provide a higher-level abstraction than the raw, low-level calls made by service clients

import boto3

s3resource = boto3.resource('s3')
bucket = s3resource.Bucket('lambdas3fun')
for object in bucket.objects.all():
    print(object.key, object.last_modified)
