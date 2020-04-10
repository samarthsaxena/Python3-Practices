import boto3

s3 = boto3.client('s3')

print(s3)
print(type(s3))
file_name = "C:\\Users\\sasaxena\\Downloads\\rtlwifi_new.zip"

bucket_name = "samarthbucket"

x= s3.upload_file(file_name, bucket_name, file_name)
print(x)
