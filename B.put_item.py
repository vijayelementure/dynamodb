import boto3
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('fueblockapp')   



# {"data":{"jid":118,"uid":"84:f7:3:67:79:b0","app":"door_gateway","evt":{"etm":"2022-03-167T11:17:21Z","dsd":4865}},"meta":{"ver":"1.0"}}

ht = table.put_item(
    Item={
        "deviceid":"FA2022V01MDRN00000005",
        "version": "1",
        "lock_status": True,
        "building_metadata": {
            "installed_date": "2022-10-20",
            "installed_time": "20:51:10",
            "location": "modern spaaces"
        },
        "last_updated": "2022-10-20T20:51:10",
        "last_updated_by": "78912"
        }
)