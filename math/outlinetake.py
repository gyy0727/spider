import statistics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def Judge_outlier(s):
    df = pd.read_excel(r"C:\Users\mu'qiu\Desktop\数据文件.xls")
    data1 = df[s]
    std_dev = statistics.stdev(data1)
    mean_value = sum(data1) / len(data1)
    outlier = []
    for i in range(0, 80):
        ten = []
        k = i
        for k in range(k, k + 20):
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
    list2 = []
    [list2.append(i) for i in outlier if not i in list2]
    return list2


def plow(s):
    df = pd.read_excel(r"C:\Users\mu'qiu\Desktop\数据文件.xls")
    data1 = np.array(df[s])
    data2 = np.array(df['day'])
    y1 = np.zeros(100)
    outlier = []
    indexoutlier = []
    outlier = Judge_outlier(s)
    indexoutlier = retakeindex(outlier, s)
    plt.figure(figsize=(30, 30), dpi=200)

    # 零分界线
    plt.plot(data2, y1, label='输出与输入差为0')
    plt.plot(data2, data1, color='black', alpha=0.3, linestyle='--', linewidth=5, marker='.', markeredgecolor='black',
             markersize='20', markeredgewidth=5, label=s)

    plt.scatter(indexoutlier, outlier, s=1000, c='red', edgecolors='black', linewidth=1, alpha=0.7, marker="s")
    plt.legend(loc='best', fontsize=18, ncol=2, bbox_to_anchor=(0.8, 0.07))
    plt.xlabel("日期", fontsize=18)
    plt.ylabel("输入水流量和输出水流量之差")  # 对横纵轴进行说明
    plt.tick_params(labelsize=14)  # 设置标签字体大小
    plt.xticks(range(0, 100, 1))
    plt.yticks(range(-15, 25, 5))
    plt.tight_layout()

    plt.savefig("R_W_20_" + s + ".jpg")
    # plt.show()


def retakeindex(a, s):
    indexoutlier = []
    df = pd.read_excel(r"C:\Users\mu'qiu\Desktop\数据文件.xls")
    data1 = df[s]
    for i in a:
        b = list(data1).index(i)
        print(b)
        indexoutlier.append(b + 1)
    print(indexoutlier)
    return indexoutlier


def main():
    list = ["region_1", "region_2", "region_3", "region_4", "region_5", "region_6", "region_7", "region_8"]
    for i in list:
        plow(i)


if __name__ == "__main__":
    main()
# 11
