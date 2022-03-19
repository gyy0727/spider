import requests
from selenium import webdriver
import  re

def main():
    please()

def please():
    browser = webdriver.Chrome()
    browser.get(url='https://pic.sogou.com/pics?st=255&from=vr&query=%E7%BE%8E%E5%A5%B3&rawQuery=%E7%BE%8E%E5%A5%B3')
    ress = re.findall(r'.*(http.+.jpg?).*', browser.page_source)
    browser.close()
    download(ress)





def download(ress):
    i=1
    for res in ress:
        print(res)
        img_url = res
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.96.400 QQBrowser/10.9.4619.400'
        }
        response = requests.get(url=img_url, headers=headers)
        img_data = response.content
        with open('%s.jpg' %(i), 'wb') as fp:
            fp.write(img_data)
            fp.close()
        i=i+1




if __name__ == "__main__":
    main()
