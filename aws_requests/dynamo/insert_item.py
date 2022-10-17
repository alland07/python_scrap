import datetime
import boto3
import uuid

db = boto3.resource('dynamodb')
table = db.Table('Poems')


def insertDB(title, nb_words, nb_the, nb_be):
  table.put_item(
    Item={
      'id': uuid.uuid4().__str__(),
      'title': title,
      'nb_words': nb_words,
      'nb_the': nb_the,
      'nb_be': nb_be,
      'date': datetime.datetime.now().__str__()
    }
  )