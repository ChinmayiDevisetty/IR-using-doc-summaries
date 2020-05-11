# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:46:36 2019

@author: ChinmayiDevisetty
"""

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import urllib.request
from urllib.request import urlopen
import requests
fname="test2.txt"
with open(fname,'r', encoding="utf8", errors='ignore') as myfile:
  text1 = myfile.read()
def get_only_text(url):
  page=urlopen(url)
  soup=BeautifulSoup(page,"html.parser")
  text=' '.join(map(lambda p: p.text,soup.find_all('p')))
  return soup.title.text,text

print ('Keywords:')
#print (keywords(text1))
print('summary:')
print(summarize(text1,ratio=0.075))