import boto3

#Create a client
s3 = boto3.client('s3')

#call s3 client to get a response from s3
response = s3.list_buckets()

print('Response from s3 client:')
print(type(response))

print()

for key, value in response.items():
    print(key,": ",value)
