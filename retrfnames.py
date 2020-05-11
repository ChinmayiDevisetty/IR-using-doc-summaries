__author__ = 'Nick Hirakawa'

import re
import os
path="/wikidocspy"
#path="summaries/"
file=open("filenames.txt","w")
for i in os.listdir('wikidocspy'):
    if i.endswith('.txt'):
        file.write(i)
        file.write("\n")
file.close()
