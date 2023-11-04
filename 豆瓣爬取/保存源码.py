import re
import requests
import xlwt
url="http://10.0.3.2/a79.htm?wlanuserip=10.39.5.30&wlanacname=&wlanacip=172.16.254.2/eportal/?c=ACSetting&a=Login"
params={
'authuserfield':'3121005178',
'authpassfield':'12345678Lx'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.205.400 QQBrowser/12.0.5435.400'

}
response = requests.get(url=url,headers=headers,params=params)
res=response.text
print(res)


