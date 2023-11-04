import re
import requests
from selenium import webdriver
import xlwt

def yuanam():#提取源码
    browser = webdriver.Edge()
    browser.get(url='http://222.200.122.247:7780/')
    a=browser.page_source
    # finding(a)
    browser.close()



def xiazai(url):#下载照片
    img_url = 'url'
    headers = {
        'cookie': 'ASP.NET_SessionId=y4qjit45stn3w3q55pdsd345',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    proxies = {
        'http': '10.20.199.28:8080',
    }
    response = requests.get(url=img_url, headers=headers,proxies=proxies)
    img_data = response.content
    with open('url.jpg', 'wb') as fp:
        fp.write(img_data)

def finding(html):#找出网址
    htm=html
    res=re.findall(r'.*?(http.+.jpg?).+',htm)
    int
    i=1
    for i in res:
        xiazai(res[i])



def main():
    yuanam()

if __name__=="__main__":
    main()
