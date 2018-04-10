# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:04:18 2018

@author: Agung Nursatria
"""

import numpy as np
from copy import deepcopy
from euclidean import euclid

def initCentroid(data,k):
    x_centroid = np.random.randint(0, np.max(data), size=k)
    y_centroid = np.random.randint(0, np.max(data), size=k)
    centroid = np.array(list(zip(x_centroid, y_centroid)), dtype=np.float32)
    return centroid

def clustering(data, centroid, k):
    old_centroid = np.zeros(centroid.shape)
    centers = np.zeros(len(data))
    sameLocation = euclid(centroid, old_centroid, None)
    # dinyatakan lokasi sama jika samelocation = 0
    while sameLocation != 0:
        for i in range(len(data)):
            distances = euclid(data[i], centroid)
            center = np.argmin(distances)
            centers[i] = center
        old_centroid = deepcopy(centroid)
        for i in range(k):
            titik = [data[j] for j in range(len(data)) if centers[j] == i]
            centroid[i] = np.mean(titik, axis=0)
        sameLocation = euclid(centroid, old_centroid, None)
    return centers