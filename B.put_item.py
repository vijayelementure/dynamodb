import boto3
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('lock_ver1')   


# {"data":{"jid":118,"uid":"84:f7:3:67:79:b0","app":"door_gateway","evt":{"etm":"2022-03-167T11:17:21Z","dsd":4865}},"meta":{"ver":"1.0"}}

table.put_item(
            Item={
            "username":"vijay",
            "password":"bhaskar",
            "data": {"jid":119,"uid":"84:f7:3:67:79:b0","app":"door_gateway","evt":{"etm":"2022-03-167T11:17:21Z","dsd":4865}},
            "meta": {"ver":"1.0"}
        }

)