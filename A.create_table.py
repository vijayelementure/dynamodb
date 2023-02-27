import boto3
import os
from dotenv import load_dotenv

load_dotenv()


dynamodb = boto3.resource('dynamodb',region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.create_table(
    TableName='keshav',
    KeySchema=[
        {
            'AttributeName': 'P_key',
            'KeyType': 'HASH'
        },
         {
             'AttributeName': 'S_key',
             'KeyType': 'RANGE'
         }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'P_key',
            'AttributeType': 'S'
        },
         {
             'AttributeName': 'S_key',
             'AttributeType': 'S'
         },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)





print(table.item_count)