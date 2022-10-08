import boto3 
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('lock_ver1')

with table.batch_writer() as batch:
    
    batch.put_item(Item={
            'userid': 'bharath',
            'gameid': 'game1',
            'high score':10500,
            'score date':2011-10-20,
        })

    batch.put_item(Item={
            'userid': 'bharath',
            'gameid': 'game2',
            'high score':12000,
            'score date':2012-1-10,
        })
    
    batch.put_item(Item={
            'userid': 'guru',
            'gameid': 'game3',
            'high score':20000,
            'score date':2012-2-12,
        })
    
    batch.put_item(Item={
            'userid': 'bharath',
            'gameid': 'game4',
            'high score':20000,
            'score date':2012-2-12,
        })
    
    batch.put_item(Item={
            'userid': 'guru',
            'gameid': 'game5',
            'high score':20000,
            'score date':2012-2-12,
        })
    
    batch.put_item(Item={
            'userid': 'bharath',
            'gameid': 'game6',
            'high score':20000,
            'score date':2012-2-12,
        })