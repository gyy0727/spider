from sklearn.cluster import DBSCAN
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False



df = pd.read_excel(r"C:\Users\mu'qiu\Desktop\数据文件.xls")
a = df['region_1']
b = df['region_2']
c = df['region_3']
d = df['region_4']
e = df['region_5']
f = df['region_6']
g = df['region_7']
h = df['region_8']
a2 = df['day']



data1 = np.array(a)
data2 = np.array(b)
data3 = np.array(c)
data4 = np.array(d)
data5 = np.array(e)
data6 = np.array(f)
data7 = np.array(g)
data8 = np.array(h)
data9 = np.array(a2)

DATA=np.vstack((data4,data9)).T


X = DATA
y = digits.target





knn_classifier = KNeighborsClassifier(n_neighbors=6)
knn_classifier.fit(X_train,y_train)

#得到评分数据
knn_classifier.score(X_test,y_test)
best_score = 0.0
best_k = -1
for k in range(1,11):
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train,y_train)
    score = knn_classifier.score(X_test,y_test)
    print("k={}, score={}".format(k, score))

    if score > best_score:
        best_k = k
        best_score = score

print("best_k =",best_k)
print("best_score =",best_score)









best_score = 0.0
best_k = -1
for k in range(1,11):
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(data1,data9)
    score = knn_classifier.score(X_test,y_test)
    print("k={}, score={}".format(k, score))

    if score > best_score:
        best_k = k
        best_score = score

print("best_k =",best_k)
print("best_score =",best_score)
