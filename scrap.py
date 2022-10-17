import re
import requests
from bs4 import BeautifulSoup

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
        results.append({
          'title' : h3.text,
          'words': words,
          'data': poem_text.replace('\n', '').strip(),
        })
    
    for element in results:
      print(element)
    
  except Exception as error:
    print(error)

def count_words(str_words):
  return len(str_words.split(' '))
  
handler()