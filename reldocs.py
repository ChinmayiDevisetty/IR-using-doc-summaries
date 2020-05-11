

import re
import os
import wikipedia
path="wikidocspy/"
pat="wikidocspy2/"
#path="summaries/"
file=open("filenames.txt","r")
topics=open("wikidocspy/topics.txt")
rel=open("wikidocspy/reldocs.txt","w")
j=1
docs=file.readlines()
queries=topics.readlines()
docs = [x.strip() for x in docs]
queries = [x.strip() for x in queries] 
for x in queries:
    l=wikipedia.search(x)
    rel.write(str(j))
    rel.write("\t")
    print(l)
    for y in l:
        y=y+".txt"
        for z in range(len(docs)):
            #print(docs[z])
            if docs[z]==y:
                rel.write(str(z+1))
                rel.write(" ")
    j=j+1            
    rel.write("\n")
rel.close()
#for i in os.listdir('wikidocspy'):
 #   if i.endswith('.txt'):
     
