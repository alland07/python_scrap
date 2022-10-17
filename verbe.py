from nltk.stem.snowball import EnglishStemmer, FrenchStemmer
import nltk

def be_verb(str_words, txt, stem_language):
  count = 0
  results = []
  stemmer = stem_language
  for word in txt.split(' '):
    stem = stemmer.stem(word)
    if stem == stemmer.stem(str_words) or word.startswith(str_words):
      if nltk.pos_tag([word])[0][1] in ['VB','VBN','VBG']:
        count += 1
        results.append(word)
  return results