import requests
import re
import xlwt
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


url="https://movie.douban.com/top250"
params={
    "start":0,
    "filter":25
}
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.96.400 QQBrowser/10.9.4619.400"
}
response=requests.get(url=url,params=params,headers=headers)
#print(response.text)
#res=re.findall(r'<p class="">.+?导演(.+)?&nbsp;&nbsp;&nbsp;主演',response.text,re.S)
res = re.findall(r'<p class="">.*?(导演.*?)&nbsp;&nbsp;&nbsp;(主演.+?)...<br>', response.text,re.S)
#bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
#data.append(bd.strip())  # strpe()为去掉前后的空格

print(res[2])