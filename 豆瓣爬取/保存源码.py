import re
import requests
import xlwt
url="https://movie.douban.com/top250"
params={
 'start': '0',
 'filter': '25'
}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.96.400 QQBrowser/10.9.4619.400',
}
response = requests.get(url=url,params=params,headers=headers)
res=re.findall(r'<span class="inq">?([^x00-xff]*)?</span>?',response.text)
print(res)
for re in res:

