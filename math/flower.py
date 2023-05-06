import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.cluster import DBSCAN

iris = datasets.load_iris()
X = iris.data[:, :3]  # #表示我们只取特征空间中的4个维度
print(X.shape)
# 绘制数据分布图


dbscan = DBSCAN(eps=0.4, min_samples=9)
dbscan.fit(X)
label_pred = dbscan.labels_
print(label_pred)

# 绘制k-means结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend(loc=2)
plt.show()

# [ 0  0  0  0  0  0  0  0  0  0  0  0  0 -1 -1 -1  0  0  0  0  0  0 -1  0
#   0  0  0  0  0  0  0  0  0 -1  0  0  0  0  0  0  0 -1  0  0  0  0  0  0
#   0  0  2  1  1  1  1  1  1 -1  2  1 -1  1 -1  1 -1  2  1  1 -1  1  1  1
#   1  1 -1  2  2  1  1 -1  1  1  1  1 -1 -1  2 -1  1  1  1  1  1 -1  1  1
#   1  1 -1  1 -1  1  1  1  1 -1 -1 -1 -1 -1  1  1  1  1  1  1  1 -1 -1 -1
#   1 -1 -1  1  1 -1  1  1  1  1 -1 -1  1  1 -1 -1  1  1  1  1  1  1  1  1
#   1  1  1  1  1  1]