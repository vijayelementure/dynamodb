import boto3 
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('lock_ver1')

with table.batch_writer() as batch:
    
    batch.put_item(Item={
            'account_type': 'savings',
            'username': 'vijay',
            'middle_name': 'bhaskar',
            'password': 'shetty',
            'address': {
                'road': 'sira road',
                'city': 'tumkur',
                'state': 'karnataka',
                'zipcode': 572106
            }
        })

    batch.put_item(
        Item={
            'account_type': 'savings',
            'username': 'vaishnavi',
            'middle_name': 'kaggal',
            'password': 'shetty',
            'address': {
                'road': 'sira road',
                'city': 'tumkur',
                'state': 'karnataka',
                'zipcode': 572106
            }
        }
    )