# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 08:39:51 2018

@author: Agung Nursatria 1301150073
"""
# -------------------------------------------------------------


#   JIKA LAMA SEPERTI MUNCUL KALIMAT DIBAWAH, BISA DIULANG JALAN PROGRAMNYA...
#   RuntimeWarning: Mean of empty slice.
#   RuntimeWarning: invalid value encountered in double_scalars


# -------------------------------------------------------------

import numpy as np
from matplotlib import pyplot as plt
from elbow import optimal_k
from kmeans import initCentroid,clustering

# Load data dan jadikan array
data = np.loadtxt('TrainsetTugas2.txt')
x_data = data[:,0]
y_data = data[:,1]

k= optimal_k(data)

# koordinat X,Y centroid data random
centroid = initCentroid(data,k)

# clustering
clusters = clustering(data,centroid,k)
    
# Buat Plot
colors = ['blue', 'forestgreen', 'red', 'darkgoldenrod', 'purple', 'cyan']
fig, ax = plt.subplots()
print('cluster')
print('total\t:', len(data),'titik')
for i in range(k):
        titik = np.array([data[j] for j in range(len(data)) if clusters[j] == i])
        print(i,'\t:',len(titik),'titik')
        ax.scatter(titik[:, 0], titik[:, 1], s=7, c=colors[i])
ax.scatter(centroid[:, 0], centroid[:, 1], marker='s', s=100, c='black')
         
# simpan result ke txt
result = []
result = np.column_stack((data, clusters))
np.savetxt('result_trains.txt', result, newline='\r\n', fmt="%s\t%s\t%i")