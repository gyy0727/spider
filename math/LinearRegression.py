import pandas as pd
from sklearn.linear_model import LinearRegression # 导⼊线性回归模型
from sklearn.metrics import r2_score

regr = LinearRegression() # 建⽴线性回归模型
import numpy as np
import matplotlib.pyplot as plt

s = "region_8"
df = pd.read_excel(r"C:\Users\mu'qiu\Desktop\数据文件.xls")
data1 = df[s]
a=[]
b=[]
for i in range(0, 70):
    ten = []
    day=[]
    k = i
    for k in range(k, k + 30):
        ten.append(data1[k])
        day.append(k)
    day=np.array(day)
    ten=np.array(ten)
    # 直接采用线性回归拟合
    lin_reg = LinearRegression()
    lin_reg.fit(day.reshape(-1,1), ten)
    y_predict = lin_reg.predict(day.reshape(-1,1))
    # 比较真值和预测值的r2
    slope = lin_reg.coef_[0]
    r = r2_score(ten, y_predict)  # 评价指标r2分数
    if (slope>0):
        if (r>0.1):
            a.append(i+1)
            print(i+1)
    # a.append(slope)
    # b.append(r)




import xlsxwriter as xw

fileName = s+'lineday.xlsx'
# xlsxwriter库储存数据到excel
workbook = xw.Workbook(fileName)  # 创建工作簿
worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
worksheet1.activate()  # 激活表
# title = ["斜率",'R']  # 设置表头
title = ['日期']  # 设置表头
worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
i = 2  # 从第二行开始写入数据
# for j in range(len(a)):
#     insertData = [a[j],b[j]]
#     row = 'A' + str(i)
#     worksheet1.write_row(row, insertData)
#     i += 1
for j in range(len(a)):
    insertData = [a[j]]
    row = 'A' + str(i)
    worksheet1.write_row(row, insertData)
    i += 1
workbook.close()  # 关闭表
#11