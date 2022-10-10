import boto3
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name =os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('fueblockapp') 



received = table.get_item(
    Key={
        'deviceid': 'FA2022V01MDRN00000001'
    }
)
item = received['Item']['deviceid']
print(item)


# print("real data")
# # print(item)
# print(type(item))

# print("\n")

# # methods of dictionary applied for fetched data
# print("only values")
# print(item.values())

# print("\n")

# print(item.popitem())

# print("\n")

# print(item.pop("username"))

# print("\n")

# print(item.keys())

# print("\n")

# print(item.items())

# print("\n")

# print(item.get("username"))

# print("\n")

