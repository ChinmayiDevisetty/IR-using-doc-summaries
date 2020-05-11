# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:08:18 2019

@author: ChinmayiDevisetty
"""

import math

def Euclidean_distance(feat_one, feat_two):

    squared_distance = 0

    #Assuming correct input to the function where the lengths of two features are the same

    for i in range(len(feat_one)):

            squared_distance += (feat_one[i] – feat_two[i])**2

    ed = sqrt(squared_distances)

    return ed;

class K_Means:

	def __init__(self, k =3, tolerance = 0.0001, max_iterations = 500):
		#self.k = k
		#self.tolerance = tolerance
		#self.max_iterations = max_iterations
        centroids=[]
        for i in range(k):
            centroids[i] = data[i]
        for i in range(max_iterations):
    		classes = {}
    		for i in range(k):
    			classes[i] = []
    
    		#find the distance between the point and cluster; choose the nearest centroid
        		for features in data:
        			distances = [np.linalg.norm(features - centroids[centroid]) for centroid in centroids]
        			classification = distances.index(min(distances))
        			classes[classification].append(features)
                    previous = dict(centroids)
    
            #average the cluster datapoints to re-calculate the centroids
                for classification in =classes:
                    centroids[classification] = np.average(classes[classification], axis = 0)
                isOptimal = True
                for centroid in self.centroids:
                    original_centroid = previous[centroid]
                    curr = centroids[centroid]
                    if np.sum((curr - original_centroid)/original_centroid * 100.0) > self.tolerance:
        		    isOptimal = False
        	
                if isOptimal:
                    break;
                                                                                                                                        