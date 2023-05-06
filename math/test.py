import statistics

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False





# plt.plot([1,2,3,4]) #默认以列表的索引作为x，输入的是y
# plt.ylabel('y')
# plt.xlabel("x轴")
# plt.show()
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
y1 = np.zeros(100)
a1 = np.array(a)

plt.figure(figsize=(30, 30), dpi=200)
plt.plot(a2, y1,label='输出与输入差为0')


# plt.plot(a2,a, c = 'k', ls = '-.', marker = 'D', lw = 2)
# plt.plot(a2,b, c = 'k', ls = '-.', marker = 'D', lw = 2)
# plt.plot(a2,c, c = 'k', ls = '-.', marker = 'D', lw = 2)
# plt.plot(a2,d, c = 'k', ls = '-.', marker = 'D', lw = 2)
# plt.plot(a2,e, c = 'k', ls = '-.', marker = 'D', lw = 2)
# plt.plot(a2,f, c = 'k', ls = '-.', marker = 'D', lw = 2)
# plt.plot(a2,g, c = 'k', ls = '-.', marker = 'D', lw = 2)
# plt.plot(a2,h, c = 'k', ls = '-.', marker = 'D', lw = 2)

s="region_8"
plt.plot(a2,h, color='red', alpha=0.3, linestyle='--', linewidth=5, marker='o', markeredgecolor='r',
         markersize='20', markeredgewidth=5,label=s)
# plt.plot(9,3.42081, color='black', alpha=0.3, linestyle='--', linewidth=5, marker='.', markeredgecolor='b',
#          markersize='30', markeredgewidth=8,label=s)
# plt.plot(a2, b, color='green', alpha=0.3, linestyle='--', linewidth=5, marker='o', markeredgecolor='r', markersize='20',
#          markeredgewidth=5,label='region_2')
# plt.plot(a2, c, color='blue', alpha=0.3, linestyle='--', linewidth=5, marker='o', markeredgecolor='r', markersize='20',
#          markeredgewidth=5,label='region_3')
# plt.plot(a2, d, color='grey', alpha=0.3, linestyle='--', linewidth=5, marker='o', markeredgecolor='r', markersize='20',
#          markeredgewidth=5,label='region_4')
# plt.plot(a2, e, color='black', alpha=0.3, linestyle='--', linewidth=5, marker='o', markeredgecolor='r', markersize='20',
#          markeredgewidth=5,label='region_5')
# plt.plot(a2, f, color='orange', alpha=0.3, linestyle='--', linewidth=5, marker='o', markeredgecolor='r',
#          markersize='20', markeredgewidth=5,label='region_6')
# plt.plot(a2, g, color='purple', alpha=0.3, linestyle='--', linewidth=5, marker='o', markeredgecolor='r',
#          markersize='20', markeredgewidth=5,label='region_7')
# plt.plot(a2, h, color='yellow', alpha=0.3, linestyle='--', linewidth=5, marker='o', markeredgecolor='r',
#          markersize='20', markeredgewidth=5,label='region_8')

# all={a,b,c,d,e,f,g,h}
# for i in all:
#     draw(y1,i)
plt.legend(loc='best',fontsize=18, ncol=2, bbox_to_anchor=(0.8, 0.07))
plt.xlabel("日期",fontsize = 18)
plt.ylabel("输入水流量和输出水流量之差") #对横纵轴进行说明
plt.tick_params(labelsize = 14) #设置标签字体大小
plt.xticks(range(0, 100, 1))
plt.yticks(range(-15, 25, 5))
plt.tight_layout()
# plt.savefig("a.jpg")
# plt.savefig("b.jpg")
# plt.savefig("c.jpg")
# plt.savefig("d.jpg")
# plt.savefig("e.jpg")
# plt.savefig("f.jpg")
# plt.savefig("g.jpg")

plt.savefig(s+".jpg")
plt.show()
