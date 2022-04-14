import requests
from selenium import webdriver
import  re
import xlrd

def main():
    for i in range(1,45):
        work_book = xlrd.open_workbook('wenxiong.xls')
        sheet_1 = work_book.sheet_by_name('wenxiong')
        cell_0_value = sheet_1.cell_value(i, 1)
        a='http:'+cell_0_value
        download(a, i)
        print(cell_0_value)


def download(res,i):
    img_url = res
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.96.400 QQBrowser/10.9.4619.400'
    }
    response = requests.get(url=img_url, headers=headers)
    img_data = response.content
    with open('%d.jpg'%(i), 'w') as fp:
        fp.write(img_data)



if __name__ == "__main__":
    main()
