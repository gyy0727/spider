import requests	 #导入请求包
import re 	#正则

url = "https://movie.douban.com/top250"
#添加User-Agent
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
resp = requests.get(url, headers=headers) #获取响应数据
page_content = resp.text #提取源代码

#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>.*?(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<people>.*?)人评价</span>', re.S) #书写正则表达式(关键在于寻找定位标签)
result = obj.finditer(page_content)#利用正则来提取数据，将电影名称存放在name组，年份存在year组，评分存在score组，评价人数存在people组(返回迭代器)

for i in result:
    print(i.group("name"))
    print(i.group("year").strip())  # 去除year的多余空格
    print(i.group("score"))
    print(i.group("people"))

print("Over!")
