import boto3
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource('dynamodb',region_name =os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('lock_ver1') 



received = table.get_item(
    Key={
        'username': 'vijay',
        'password': 'bhaskar'
    }
)
item = received['Item']
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

