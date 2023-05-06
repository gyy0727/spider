import numpy as np
import pandas as pd
import statistics

s = 'region_1'
df = pd.read_excel(r"C:\Users\mu'qiu\Desktop\数据文件.xls")
data1 = df[s]
std_dev = statistics.stdev(data1)
mean_value = sum(data1) / len(data1)
outlier=[]
for i in range(0, 90):
    ten = []
    k = i
    for k in range(k, k + 10):
        ten.append(data1[k])
    if(std_dev>1):
        differ=max(ten)-min(ten)
        if(differ>(2*std_dev)):
            outlier.append(max(ten))
            outlier.append(min(ten))
    if(std_dev<1):
        differ = max(ten) - min(ten)
        if(differ>(3*std_dev)):
            outlier.append(max(ten))
            outlier.append(min(ten))

a=list(data1).index(outlier[0])
print(a)


