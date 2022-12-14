import re
import requests
from bs4 import BeautifulSoup
from nltk.stem.snowball import EnglishStemmer
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# My files
from count import count_words, count_the
from dataframe import create_dataframe
from verbe import be_verb


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
        # poem_fr = translate(poem_text)
        res_be_verb = be_verb(txt=poem_text, str_words='be', stem_language=EnglishStemmer())
        # res_etre_verb = be_verb(txt=poem_fr, str_words='etre', stem_language=FrenchStemmer())
        nb_the = count_the(poem_text, 'the')
        nb_be = len(res_be_verb)
        results.append({
          'title': h3.text,
          'words': words,
          # 'data': poem_fr,
          'the': nb_the,
          'be_verb': nb_be
        })
        # insertDB(title=h3.text, nb_words=words, nb_the=nb_the, nb_be=nb_be)

    create_dataframe(results=results)

  except Exception as error:
    print(error)


handler()
