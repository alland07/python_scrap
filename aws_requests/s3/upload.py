import boto3

s3 = boto3.resource('s3')


def upload(path='../../poem.csv'):
  bucket_name = 'big-data-a5'
  file_name = 'poem.csv'
  flags = 'rb'
  try:
    s3.Object(bucket_name, file_name).put(Body=open(path, flags))
  except Exception as e:
    print(e)


upload()