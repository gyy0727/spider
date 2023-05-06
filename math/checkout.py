import statistics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

s = "region_8"
df = pd.read_excel(r"C:\Users\mu'qiu\Desktop\数据文件.xls")
data1 = df[s]
std_dev = statistics.stdev(data1)
mean_value = sum(data1) / len(data1)
outlier = []
for i in range(0, 90):
    ten = []
    k = i
    for k in range(k, k + 10):
        ten.append(data1[k])
    if (std_dev > 1):
        differ = max(ten) - min(ten)
        if (differ > (2 * std_dev)):
            outlier.append(max(ten))
            outlier.append(min(ten))
    if (std_dev < 1):
        differ = max(ten) - min(ten)
        if (differ > (4 * std_dev)):
            outlier.append(max(ten))
            outlier.append(min(ten))

    outlier=list(set(outlier))

indexoutlier = []
for i in outlier:
    b = list(data1).index(i)
    print(b)
    indexoutlier.append(b + 1)
print(indexoutlier)

import xlsxwriter as xw
data=data1
fileName = s+'2.xlsx'
# xlsxwriter库储存数据到excel
workbook = xw.Workbook(fileName)  # 创建工作簿
worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
worksheet1.activate()  # 激活表
title = ["日期",'异常值']  # 设置表头
worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
i = 2  # 从第二行开始写入数据
for j in range(len(outlier)):
    insertData = [outlier[j],indexoutlier[j]]
    row = 'A' + str(i)
    worksheet1.write_row(row, insertData)
    i += 1
workbook.close()  # 关闭表


#1111