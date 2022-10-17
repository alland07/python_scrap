import pandas as ps
import matplotlib.pyplot as plt

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
