from sklearn.cluster import DBSCAN
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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

DATA=np.vstack((data2,data9)).T

# 构建DBSCAN聚类模型
dbscan = DBSCAN(eps=5, min_samples=4)
labels = dbscan.fit_predict(DATA)

# 输出聚类结果
# for i in range(max(labels) + 1):
#     print(f"Cluster {i + 1}: {list(DATA[labels == i])}")
# print(f"Noise: {list(DATA[labels == -1])}")

print('聚类结果:', labels)
x0 = DATA[labels == 0]
x1 =DATA[labels == 1]
x2 = DATA[labels == -1]
plt.scatter(x0[:, 1], x0[:, 0], c="red", marker='.', label='label0')
plt.scatter(x1[:, 1], x1[:, 0], c="green", marker='.', label='label1')
plt.scatter(x2[:, 1], x2[:, 0], c="blue", marker='.', label='label2')
plt.xlabel('日期')
plt.ylabel('输入水量与输出水量之差')
plt.legend(loc='best')
plt.show()
