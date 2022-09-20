import boto3
import logging


s3 = boto3.resource('s3',region_name = 'ap-south-1',aws_access_key_id="AKIATZHKUJIM7W4P3EMJ",aws_secret_access_key="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")


s3.create_bucket('excel',region_name = 'ap-south-1',aws_access_key_id="AKIATZHKUJIM7W4P3EMJ",aws_secret_access_key="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")