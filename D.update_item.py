import boto3
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name =os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('acquesa_ver1') 



table.update_item(
    Key={
        'username': 'vaishu',
        'password': 'bhaskar'
    },
    UpdateExpression='SET id = :value',
    ExpressionAttributeValues={
        ':value': 78
    }
)
print("id attribute has been updated successfully")