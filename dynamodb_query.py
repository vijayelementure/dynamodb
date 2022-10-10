import boto3
from boto3.dynamodb.conditions import Key,Attr
import os
from dotenv import load_dotenv

load_dotenv()
client = boto3.client('dynamodb',region_name =os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
#dynamodb = boto3.resource('dynamodb',region_name =os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
#table = dynamodb.Table('fueblockapp') 


response = client.query(
    TableName='fueblockapp',
    Select='SPECIFIC_ATTRIBUTES',
    AttributesToGet=[
        'lock_status',
    ],
    Limit=123,
    ConsistentRead=True,
    KeyConditions={
        'lock_status': {
            'AttributeValueList': [
                {
                    'S': 'True',
                },
            ],
            'ComparisonOperator': 'EQ'
        }
    }
)
print(response['Items'])