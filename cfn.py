__author__ = 'Nick Hirakawa'

import re
import os
path="wikidocspy/"
pat="wikidocspy2/"
#path="summaries/"
file=open("filenames.txt","r")
j=1
for i in os.listdir('wikidocspy'):
    if i.endswith('.txt'):
     filename=path+str(i)
     print(filename)
     file1=open(filename,"r")
     s=file1.read()
     fn=pat+str(j)+".txt"
     file2=open(fn,"w")
     file2.write(s)
     file1.close()
     file2.close()
     j=j+1
