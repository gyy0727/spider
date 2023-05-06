from sklearn.cluster import DBSCAN
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

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

s = 'all'

data1 = np.array(a)
data2 = np.array(b)
data3 = np.array(c)
data4 = np.array(d)
data5 = np.array(e)
data6 = np.array(f)
data7 = np.array(g)
data8 = np.array(h)
data9 = np.array(a2)
DATA = np.vstack((data1, data2, data3, data4, data5, data6, data7, data8)).T
k_dist = []
for i in range(DATA.shape[0]):
    dist = (((DATA[i] - DATA) ** 2).sum(axis=1) ** 0.5)
    dist.sort()
    k_dist.append(dist[3])
    np.array(k_dist)
k = 3  # 此处k取 2*2 -1
k_dist = np.array(k_dist)
k_dist.sort()
plt.figure(figsize=(10, 10), dpi=100)  # 画布的宽是8英寸，高是4英寸；每英寸有120个像素
#
#     #（1）绘制原数据集
# plt.subplot(1, 2, 1)
# plt.plot(np.arange(k_dist.shape[0]), k_dist[::-1])
# plt.figure(figsize=(20, 10), dpi=100)
#
# # 由拐点确定邻域半径
eps = k_dist[::-1][15]
print(eps)
# plt.scatter(15, eps, color="r")
# plt.plot([0, 15], [eps, eps], linestyle="--", color="r")
# plt.plot([15, 15], [0, eps], linestyle="--", color="r")
# plt.subplot(1, 2, 2)  # 当前绘图区设定为第2格


# 改eps和min_samples
dbscan = DBSCAN(eps=eps, min_samples=4)
labels = dbscan.fit_predict(DATA)

print('聚类结果:', labels)
x0 = DATA[labels == 0]
x1 = DATA[labels == 1]
x2 = DATA[labels == -1]
x3 = DATA[labels == 2]
x4 = DATA[labels == 3]
x5 = DATA[labels == 4]
x6 = DATA[labels == 5]
x7 = DATA[labels == 6]
x8 = DATA[labels == 7]
x9 = DATA[labels == 8]

# 画散点图
plt.scatter(x0[:, 1], x0[:, 0], c="red", marker='.', label=s + ' label0')
plt.scatter(x1[:, 1], x1[:, 0], c="green", marker='*', label=s + ' label1')
plt.scatter(x2[:, 1], x2[:, 0], c="blue", marker='^', label=s + ' label2')
plt.scatter(x3[:, 1], x3[:, 0], c="black", marker='s', label=s + ' label3')
plt.scatter(x4[:, 1], x4[:, 0], c="yellow", marker='p', label=s + ' label4')
plt.scatter(x5[:, 1], x5[:, 0], c="purple", marker='h', label=s + ' label5')
plt.scatter(x6[:, 1], x6[:, 0], c="orange", marker='+', label=s + ' label6')
plt.scatter(x7[:, 1], x7[:, 0], c="pink", marker='x', label=s + ' label7')
plt.scatter(x8[:, 1], x8[:, 0], c="grey", marker='D', label=s + ' label8')
plt.scatter(x9[:, 1], x9[:, 0], c="brown", marker='3', label=s + ' label9')
plt.xlabel('日期')
plt.ylabel('输入水量与输出水量之差')
plt.legend(loc='best')
plt.savefig(s + ".jpg")
plt.show()
