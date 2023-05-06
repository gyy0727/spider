import numpy
import numpy as np
import matplotlib.pyplot as plt
import numpy as numpy
import pandas as pd
from matplotlib.font_manager import FontProperties
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.metrics import silhouette_score
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

#肘部法1
# K = range(1, 10)
# mean_distortions = []
# for k in K:
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit_predict(data1.reshape(-1,1))
#     mean_distortions.append(
#         sum(
#             np.min(
#                 cdist(data1.reshape(-1,1), kmeans.cluster_centers_, metric='euclidean'), axis=1))
#         / data1.reshape(-1,1).shape[0])
#
# plt.plot(K, mean_distortions,marker=".")


#############肘部法2
# distortions = []  # 用来存放设置不同簇数时的SSE值
# for i in range(2, 11):
#     kmModel = KMeans(n_clusters=i)
#     kmModel.fit_predict(data1.reshape(-1,1))
#     distortions.append(kmModel.inertia_)  # 获取K-means算法的SSE
#     # 绘制曲线
# plt.plot(range(2, 11), distortions, marker="o")

#############轮廓系数法
# sil_score = []
# for k in range(2, 9):
#     kmeans = KMeans(n_clusters=k, random_state=0).fit_predict(data1.reshape(-1,1))
#     sil_score.append(silhouette_score(data1.reshape(-1,1), kmeans))
# plt.plot(range(2, 9), sil_score, 'o-')
# #############





# X = np.vstack((data1,data2,data3,data4,data5,data6,data7,data8)).T
# # # print(X)
# K = range(1, 10)
# mean_distortions = []
# for k in K:
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit_predict(X.reshape(-1,1))
#     mean_distortions.append(
#         sum(
#             np.min(
#                 cdist(X.reshape(-1,1), kmeans.cluster_centers_, metric='euclidean'), axis=1))
#         / X.reshape(-1,1).shape[0])
# plt.plot(K, mean_distortions, 'bx-')

plt.xlabel('k')
plt.ylabel('平均畸变程度')
plt.show()
