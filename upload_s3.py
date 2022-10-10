import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3_client = boto3.s3_client('s3',region_name = os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))