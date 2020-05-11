from sklearn.metrics import silhouette_score
import numpy as np
import pandas as pd
from scipy.stats import entropy
df = pd.read_csv("Book2.csv")
#df = df[['one', 'two']]
dataset = df.astype(float).values.tolist()

X = df.values
print(X)
print(len(X))
def jensen_shannon(query, matrix):
    # lets keep with the p,q notation above
    p = np.asarray(query) # take transpose
    q = np.asarray(matrix) # transpose matrix
    m = 0.5*np.add(p,q)
    l=0.5*(entropy(p,m)+entropy(q,m))
    return np.sqrt(abs(l))
dist=[]
for i in range(len(X)):
    a=[]
    for j in range(len(X)):
        a.append(jensen_shannon(X[i],X[j]))
    dist.append(a)

for n_cluster in range(2, len(X)-1):
    kmeans,centroids = K_Means(X,n_cluster,0.0001,500)
    print(len(X))
    print(len(kmeans))
    #label = kmeans.labels_
    sil_coeff = silhouette_score(dist, kmeans, metric='precomputed')
    print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))
    
"""from sklearn.metrics import pairwise_distances
from sklearn import datasets
dataset = datasets.load_iris()
X = dataset.data
y = dataset.target
import numpy as np
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
labels = kmeans_model.labels_
print(len(X))
print(len(y))
print(len(labels))
print(metrics.silhouette_score(X, labels, metric='euclidean'))
"""