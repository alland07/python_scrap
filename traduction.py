from transformers import pipeline

def translate(text):
  pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-fr")
  return pipe(text)[0]["translation_text"]