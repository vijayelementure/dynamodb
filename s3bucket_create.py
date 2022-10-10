import boto3 
import os
from dotenv import load_dotenv

load_dotenv()


s3_client = boto3.client('s3',region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

response = s3_client.create_bucket(
    ACL='private',
    Bucket='profilepictureobject',
      CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
    )


print(response)