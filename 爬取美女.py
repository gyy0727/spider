import requests
import re

url="https://pic.sogou.com/pics?st=255&from=vr&query=%E7%BE%8E%E5%A5%B3&rawQuery=%E7%BE%8E%E5%A5%B3"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.96.400 QQBrowser/10.9.4619.400"
}
response=requests.get(url=url,headers=headers)
print(response.text)
'''
def(url)
    img_url = 'https://img04.sogoucdn.com/app/a/100520093/f9d5c084396d06f6-0c7006bf1d0bb8d5-44cfb308fd53675f90401be304dc572d.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.96.400 QQBrowser/10.9.4619.400'
    }
    response = requests.get(url=img_url, headers=headers)
    img_data = response.content
    with open('1.jpg', 'wb') as fp:
        fp.write(img_data)
'''