import re
import requests
from bs4 import BeautifulSoup
import pandas as ps
import matplotlib.pyplot as plt
from nltk.stem.snowball import EnglishStemmer
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

def handler():
  try:
    response = requests.get('https://happymag.tv/best-short-poems-of-all-time/')
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('span', attrs={"style": re.compile("text-decoration: underline;")})
    titles = [title.text for title in titles]
    
    results = []
    
    for h3 in soup.find_all('h3'):
      if h3.text in titles:
        poem_text = ''
        for sib in h3.fetchNextSiblings():
          if sib.name == 'p':
            poem_text += sib.text
          
          if sib.name == 'h3':
            break
        words = count_words(poem_text)
        poem_text = poem_text.replace('\n', ' ').strip()
        results.append({
          'title' : h3.text,
          'words': words,
          'data': poem_text,
          'the': count_the(poem_text, 'the'),
          'be_verb': len(be_verb(txt=poem_text, str_words='be'))
        })
        
    create_dataframe(results=results)
    
  except Exception as error:
    print(error)
    
def create_dataframe(results):
  columns = ['title','be_verb']
  df = ps.DataFrame(results)
  df.to_csv('poem.csv', index=False, encoding='utf-8', columns=columns)
  
  plt.rcParams["figure.figsize"] = [7.00, 3.50]
  plt.rcParams["figure.autolayout"] = True
  
  df = ps.read_csv("poem.csv", usecols=columns)
  
  df.plot(kind='bar')
  plt.ylabel('words')
  plt.xlabel('poem')
  plt.title('Analyse')
  plt.show()

def count_words(str_words):
  return len(str_words.split(' '))

def count_the(str_words, txt):
  return str_words.lower().count(txt)

def be_verb(str_words, txt):
  count = 0
  results = []
  stemmer = EnglishStemmer()
  for word in txt.split(' '):
    stem = stemmer.stem(word)
    if stem == stemmer.stem(str_words) or word.startswith(str_words):
      if nltk.pos_tag([word])[0][1] in ['VB','VBN','VBG']:
        count += 1
        results.append(word)
  print(count, results)
  return results
  
handler()