import boto3
import os
import uuid
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('userprofile') 

table.put_item(
    Item={
    "email":"vijaybhaskarmyv@gmail.com",
    "profile photo":"",
    "uuid":0,
    "Created Date": str(datetime.now())
    }

)