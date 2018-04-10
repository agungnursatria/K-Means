# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 14:22:51 2018

@author: Agung Nursatria
"""

from kmeans import clustering,initCentroid
from matplotlib import pyplot as plt

def optimal_k(data):
    # mencari daftar sse
    sse = []
    for k in range(1,8):
        centroid = initCentroid(data,k)
        clusters = clustering(data,centroid,k)
        sumtoCluster = 0
        for i in range(k):
            for j in range(len(data)):
                if clusters[j] == i:
                    # Euclidean Distance untuk sumtoCluster
                    sumtoCluster += (abs((data[j,0]-centroid[i][0])**2) +
                                     abs((data[j,1]-centroid[i][1])**2))
        sse.append([k,sumtoCluster])
    
    # Plot grafik kluster
    sseKey = [sse[j][0] for j in range(len(sse))]
    sseValue = [sse[j][1] for j in range(len(sse))]
    plt.figure()
    plt.plot(sseKey, sseValue)
    plt.xlabel("Number of k")
    plt.ylabel("SSE")
    plt.show()
    
    # mencari k optimal dengan patokan jika nilai yang berkurang lebih sama dengan 30% dari turunnya sse pertama, dianggap turun drastis dan k optimal
    k_optimal = 2
    first_drop_sse = (sse[0][1]-sse[1][1])
    for k in range(1,5):
        if (sse[k][1]-sse[k+1][1] >= (first_drop_sse*0.3)):
            k_optimal = sse[k+1][0]
    return k_optimal