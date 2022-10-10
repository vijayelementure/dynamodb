import boto3
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name =os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('fueblockapp') 



table.update_item(
    Key={
       'deviceid':'FA2022V01MDRN00000005'
    },
    UpdateExpression='SET lock_status = :value',
    ExpressionAttributeValues={
        ':value': False,
    }
)
print(" attribute has been updated successfully")