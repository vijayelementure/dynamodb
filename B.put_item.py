import boto3
import os
import uuid
from dotenv import load_dotenv
import datetime

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('keshav')   

names=["vijay","keshav","bharath","guru","gagan","vikram","rajath","sharath","thousif","jeevan"
       "pariyar","sahana","jee","anusha","vidya","anirudh","rachu","devendra","manohar","devu",
       "prasad","mahesh","vinay","vijay","bhargav","sathish","vicky","rocky","sreekar","vedanth","naveen"]

# {"data":{"jid":118,"uid":"84:f7:3:67:79:b0","app":"door_gateway","evt":{"etm":"2022-03-167T11:17:21Z","dsd":4865}},"meta":{"ver":"1.0"}}
for i in range(30):
    ht = table.put_item(
    Item={
#  "newkey": "vijaybhaskarmyv@gmail.com",
#  "datetime" : str(datetime.datetime.now()),
#   "Active Status": "running",
#  "Device Access Id": i,
#  "Hub ID": i+1,
#  "Installed Date": "2022-10-13 18:25:23.113246",
#  "uuid": i+100
 "slno":i,
 "name":names[i],
 "deviceid":i+100,
 "installationdate":str(datetime.datetime.now())
 
        }
)
