import boto3
import os
import uuid
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('fueblockapp')   




table.put_item(
    Item={
    "email":"vijaybhaskarmyv@gmail.com",
    "FullName":"vijay bhaskar",
    "mobile":9741113585,
    "HashedPassword":"dsjhgfsrjgidrgjldkgdkgg",
    "uuid":"FA2022V01MDRN00000005",
    "account created": str(datetime.now())
    }

)