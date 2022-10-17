import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
  TableName='Poems',
  KeySchema=[
    {
      'AttributeName': 'id',
      'KeyType': 'HASH'
    }
  ],
  AttributeDefinitions=[
    {
      'AttributeName': 'id',
      'AttributeType': 'S'
    },
    # {
    #   'AttributeName': 'title',
    #   'AttributeType': 'S'
    # },
    # {
    #   'AttributeName': 'number_words',
    #   'AttributeType': 'N'
    # },
    # {
    #   'AttributeName': 'number_the',
    #   'AttributeType': 'N'
    # },
    # {
    #   'AttributeName': 'number_be',
    #   'AttributeType': 'N'
    # },
  ],
  ProvisionedThroughput={
    'ReadCapacityUnits': 1,
    'WriteCapacityUnits': 1,
  }
)

print(table)
