__author__ = 'Nick Hirakawa'

import re
import os
path="wikidocspy2/"
#path="summaries/"
file=open("findex.txt","w")
j=1
for i in os.listdir('wikidocspy2'):
    if i.endswith('.txt'):
     filename=path+str(i)
     file1=open(filename,"r")
     s=file1.read()
     p=s.split(" ")
     file.write(p[0])
     file.write(" ")
     file.write(i)
     file.write("\n")
file.close()
