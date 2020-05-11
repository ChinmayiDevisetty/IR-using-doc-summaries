# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:53:10 2019

@author: ChinmayiDevisetty
"""

from kmeans2 import kmeans
import pandas as pd
import math
df = pd.read_csv(r"ipl.csv")
dataset = df.astype(float).values.tolist()
#df = df[['one', 'two']]
X = df.values #returns a numpy array
print(X)

kmeans(df,10,10)
