#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1, 1, 2], [-2, -1, -1, 1], [-3, -2, 2, 0], [1, 1, 2, 3], [2, 1, 2, 4], [3, 2, 2, 0]])
pca = PCA(n_components=4)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.singular_values_)

pca = PCA(n_components=2, svd_solver='full')
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.singular_values_)

pca = PCA(n_components=1, svd_solver='arpack')
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.singular_values_)
