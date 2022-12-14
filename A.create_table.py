import boto3
import os
from dotenv import load_dotenv

load_dotenv()


dynamodb = boto3.resource('dynamodb',region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.create_table(
    TableName='fueblockapp',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        },
        # {
        #     'AttributeName': 'gameid',
        #     'KeyType': 'RANGE'
        # }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        # {
        #     'AttributeName': 'gameid',
        #     'AttributeType': 'S'
        # },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)





print(table.item_count)