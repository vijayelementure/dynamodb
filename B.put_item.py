import boto3



dynamodb = boto3.resource('dynamodb',region_name =os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('test')   



    
table.put_item(
            Item={
            "id" : '1',
            "username":"vijay",
            "password":"vijay123",
        }
)



print(table.item_count)