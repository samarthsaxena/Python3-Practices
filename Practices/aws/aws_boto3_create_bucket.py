import boto3

s3 = boto3.client('s3')

s3.create_bucket(Bucket='boto3BucketSamarthSASASA')
