# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:01:19 2018

@author: Agung Nursatria
"""

import numpy as np

# Euclidean distance untuk banyak data centroid
def euclid(data, centroid, ax=1):
    return np.linalg.norm(data - centroid, axis=ax)