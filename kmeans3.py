# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:08:18 2019

@author: ChinmayiDevisetty
"""

import math
import pandas as pd
import numpy as np
import scipy.stats as Ss
from scipy.stats import entropy

def jensen_shannon(query, matrix):
    # lets keep with the p,q notation above
    p = np.asarray(query) # take transpose
    q = np.asarray(matrix) # transpose matrix
    m = 0.5*np.add(p,q)
    l=0.5*(entropy(p,m)+entropy(q,m))
    return np.sqrt(abs(l))

def Euclidean_distance(feat_one, feat_two):
    squared_distance = 0
    #Assuming correct input to the function where the lengths of two features are the same
    for i in range(len(feat_one)):
        t=feat_two[i]
        s=feat_one[i]-t
        squared_distance += (s)**2
    ed = math.sqrt(squared_distance)
    return ed;

def K_Means(data,k,tolerance = 0.0001,max_iterations = 500): 
    print("DATA\n",data)
    #self.k = k
	#self.tolerance = tolerance
	#self.max_iterations = max_iterations
    centroids={}
    classes = {}
    clusters={}
    for i in range(k):
        print("data:",data[i])
        centroids[i] = data[i]
    for l in range(max_iterations):
        #print(centroids)
        for i in range(k):
            classes[i] = []
            clusters[i]=[]
            labels=[]
            i=0;
        for features in data:
            distances=[]
            for s in range(k):
                distances.append(jensen_shannon(features,centroids[s]))
                #distances = [np.linalg.norm(features - centroids[centroid]) for centroid in centroids]
            classification = distances.index(min(distances))
            classes[classification].append(features)
            clusters[classification].append(i)
            labels.append(classification)
            i=i+1
            previous = dict(centroids)
        for classification in classes:
            centroids[classification] = np.average(classes[classification], axis = 0)
        isOptimal = True
        for centroid in centroids:
                original_centroid = previous[centroid]
                curr = centroids[centroid]
                if np.sum((curr - original_centroid)/original_centroid * 100.0) > tolerance:
                    isOptimal = False
    	
        if isOptimal:
            break;
    print(centroids)
    for i in range(k):
        print("cluster\n",clusters[i])
    for i in range(len(data)):
        print("label: ",labels[i])        
    return labels,centroids
df = pd.read_csv("Book2.csv")
#df = df[['one', 'two']]
dataset = df.astype(float).values.tolist()

X = df.values
print(X)
print(len(X)) #returns a numpy array
K_Means(X,4,0.001,500)                                                                                                                                       