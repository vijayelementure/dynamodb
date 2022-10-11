import boto3
import os
import uuid
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('userprofile') 

s3 = boto3.client('s3',region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

s3object = s3.generate_presigned_post('lockuserprofile','god.png')

print(s3object)

print("\n")


s3objecturl = s3object.get('url')


objectkey = s3object.get('fields').get('key')
print(objectkey)

print("\n")

print(s3objecturl)

table.put_item(
    Item={
    "email":"vijaybhaskarmyv@gmail.com",
    "profile photo":s3objecturl+objectkey,
    "uuid":0,
    "Created Date": str(datetime.now())
    }

)