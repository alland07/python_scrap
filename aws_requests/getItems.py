import boto3

db = boto3.resource('dynamodb')
table = db.Table('Poems')


def getAllItems():
  response = table.scan()
  data = response['Items']
  total_the = 0
  total_be = 0
  nbr_items = 0
  total_words = 0
  for ele in data:
    total_the += ele['nb_the']
    total_be += ele['nb_be']
    nbr_items += 1
    total_words += ele['nb_words']

  print(f"Total des the : {total_the}, total des be : {total_be}, total des mots : {total_words}, nombre d'items : {nbr_items}")
