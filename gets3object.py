import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3',region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
response = s3.get_bucket_location(
    Bucket='profilepictureobject',
    # ExpectedBucketOwner='string'
)['LocationConstraint']

print(response)

x = s3.generate_presigned_post('profilepictureobject','god.png')

print(x.get('url'))
