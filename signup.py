import boto3
import os
import uuid
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('db1')   




table.put_item(
    Item={"uuid":"ffffffff-ffff-ffff-ffff-ffffffffffff",
          "datetime":"kjhkj",
        "data":{"jid":4535,"uuid":"ffffffff-ffff-ffff-ffff-ffffffffffff",
                  "evt":{"etm":"2022-03-167T11:17:21Z","csm":20},
                  "dev":"water_measure"},"meta":{"ver":"1.0"}
   
    }

)