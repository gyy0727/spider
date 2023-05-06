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
s='region_1'
DATA=np.vstack((data1,data9)).T


k_dist = []
for i in range(DATA.shape[0]):
    dist = (((DATA[i] - DATA)**2).sum(axis=1)**0.5)
    dist.sort()
    k_dist.append(dist[3])
    np.array(k_dist)
k = 3  # 此处k取 2*2 -1
k_dist = np.array(k_dist)
k_dist.sort()
plt.figure(figsize=(8,4),dpi=120)   #画布的宽是8英寸，高是4英寸；每英寸有120个像素
#
#     #（1）绘制原数据集
# plt.subplot(1,2,1)
# plt.plot(np.arange(k_dist.shape[0]),k_dist[::-1])
#
# # 由拐点确定邻域半径
eps = k_dist[::-1][15]
print(eps)
# plt.scatter(15,eps,color="r")
# plt.plot([0,15],[eps,eps],linestyle="--",color = "r")
# plt.plot([15,15],[0,eps],linestyle="--",color = "r")



dbscan = DBSCAN(eps=eps, min_samples=3)
labels = dbscan.fit_predict(DATA)

# 输出聚类结果
# for i in range(max(labels) + 1):
#     print(f"Cluster {i + 1}: {list(DATA[labels == i])}")
# print(f"Noise: {list(DATA[labels == -1])}")

print('聚类结果:', labels)
x0 = DATA[labels == 0]
x1 =DATA[labels == 1]
x2 = DATA[labels == -1]
x3 = DATA[labels == 2]
x4 = DATA[labels == 3]
x5 = DATA[labels == 4]
plt.figure(figsize=(10, 10), dpi=100)
# plt.subplot(1,2,2)  #当前绘图区设定为第2格
plt.scatter(x0[:, 1], x0[:, 0], c="red", marker='.', label=s+' label0')
plt.scatter(x1[:, 1], x1[:, 0], c="green", marker='.', label=s+' label1')
plt.scatter(x2[:, 1], x2[:, 0], c="blue", marker='.', label=s+' label2')
plt.scatter(x3[:, 1], x3[:, 0], c="black", marker='.', label=s+' label3')
plt.scatter(x4[:, 1], x4[:, 0], c="yellow", marker='.', label=s+' label4')
plt.scatter(x5[:, 1], x5[:, 0], c="purple", marker='.', label=s+' label5')
plt.xlabel('日期')
plt.ylabel('输入水量与输出水量之差')
plt.legend(loc='best')
plt.savefig(s+".jpg")
# plt.savefig("region_2.jpg")
# plt.savefig("region_3.jpg")
# plt.savefig("region_4.jpg")
# plt.savefig("region_5.jpg")
# plt.savefig("region_6.jpg")
# plt.savefig("region_7.jpg")
# plt.savefig("region_8.jpg")

plt.show()