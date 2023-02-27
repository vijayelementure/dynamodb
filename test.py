# import boto3
# import os
# import uuid
# from dotenv import load_dotenv
# from datetime import datetime


# load_dotenv()

# dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
# table = dynamodb.Table('userprofile') 

# s3 = boto3.client('s3',region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

# s3object = s3.generate_presigned_post('lockuserprofile2','god.png')

# objectkey = s3object.get('fields').get('key')

# response = s3.get_bucket_location(
#     Bucket='lockuserprofile2',
#     # ExpectedBucketOwner='string'
# )['LocationConstraint']




# print()

# data1 = "https://"
# data2 = "lockuserprofile2"
# data3 = ".s3."
# data4 = response
# data5 = ".amazonaws.com/"
# data6 = objectkey

# profiledata = data1+data2+data3+data4+data5+data6

# table.put_item(
#     Item={
#     "email":"vijaybhaskarmyv@gmail.com",
#     "profile photo":profiledata,
#     "uuid":0,
#     "Created Date": str(datetime.now())
#     }

# )


class Testing:
    def __init__(self,x):
        print("vijay")
    
    def __init__(self):
        print("bhaskar")
        
t = Testing()




















