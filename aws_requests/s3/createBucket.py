import boto3
from botocore.exceptions import ClientError


def create_bucket():
  bucket_name = 'big-data-a5'
  region = 'eu-west-3'
  try:
    s3_client = boto3.client('s3', region_name=region)
    location = {'LocationConstraint': region}
    res = s3_client.create_bucket(Bucket=bucket_name,
                                  CreateBucketConfiguration=location)
    print(res)
  except ClientError as e:
    print(e)


create_bucket()
