import boto3
from boto3.dynamodb.conditions import Key
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name =os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('fueblockapp') 


response = table.query(
  KeyConditionExpression=Key('deviceid').eq('FA2022V01MDRN00000001')
)
print(response['Items'])
print(type(response['Items']))