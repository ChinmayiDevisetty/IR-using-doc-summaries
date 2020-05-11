from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import urllib.request
from urllib.request import urlopen
import requests

#text1 =  requests.get('https://en.wikipedia.org/wiki/Hidden_Markov_model').text
#print(text1)
#://rare-technologies.com/the_matrix_synopsus.txt
fname="documents/19970.txt"
with open(fname,'r', encoding="utf8", errors='ignore') as myfile:
 text1 = myfile.read()
print ('Keywords:')
print (keywords(text1))
print('summary:')
print(summarize(text1,ratio=0.05))
