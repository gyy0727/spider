import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

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

data1 = np.array(f)
data2 = np.array(a2)
x = np.vstack((data1, data2)).T
from sklearn.cluster import KMeans

clusters = 3  # 3个类别
model = KMeans(n_clusters=clusters)  # 构造模型
model.fit(x)  # 训练数据

# 获得各种指标
y_predict = model.labels_  # 获取聚类标签,从0开始
centers = model.cluster_centers_  # 获得中心点的坐标

# 对比数据集与聚类效果
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4), dpi=120)  # 画布的宽是8英寸，高是4英寸；每英寸有120个像素

# （1）绘制原数据集
plt.subplot(1, 2, 1)  # 画布分为1行，2列，共2格，当前绘图区设定为第1格
# 特征1绘制在横坐标，特征2绘制在纵坐标；每个样本点的颜色跟类别有关；每点像素是20，形状是圆圈。
plt.scatter(x[:, 1], x[:, 0], c=y_predict, s=20, marker='o')
plt.title("datasets")  # 标题是"datasets"

# （2）绘制k-means结果
plt.subplot(1, 2, 2)  # 当前绘图区设定为第2格
plt.title("k-means")
colors = ["g", "b", "r"]
markers = ['o', '*', '+']
for i in range(clusters):
    # （21）绘制样本点
    xi = x[y_predict == i]  # 取出第i个类别的样本点
    plt.scatter(xi[:, 1], xi[:, 0], c=colors[i], marker=markers[i], alpha=0.6)  # 绘制第i个类别的样本点，透明度是0.6
    # （22）绘制中心点
    plt.scatter(centers[i][1], centers[i][0], c='black', marker='o', alpha=0.3, s=200)  # 中心点处绘制圆圈
    plt.scatter(centers[i][1], centers[i][0], c='white', marker='$%d$' % i, s=50)  # 中心点处绘制类别数字

    # （3）显示
plt.show()
