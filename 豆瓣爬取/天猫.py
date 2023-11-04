import json
import random
import re
import time

import requests
import xlwt

'''browser = webdriver.Chrome()
browser.get(url='https://s.taobao.com/search?spm=a21bo.jianhua.201867-main.10.5af911d9lu5wsR&q=%E7%94%B7%E8%A3%85')
a=browser.page_source
print(a)
browser.close()
'''

url='http://222.200.122.247:7780/'
headers={

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}
proxies = {
    'http': '10.20.199.28:8080',
'https': '10.20.199.28:8080',
}
response=requests.get(url=url,headers=headers,proxies=proxies)
page_content = response.text


"""time.sleep(random.random())
#print(response.text)
json_str=re.findall(r'g_page_config = (.*);',response.text)[0]
json_dict=json.loads(json_str)
#print(json_str)
auctions=json_dict['mods']['itemlist']['data']['auctions']
i=1
j=1
k=1
l=1
m=1
n=1
Workbook=xlwt.Workbook(encoding='utf-8')
Worksheet=Workbook.add_sheet("taobao")
Worksheet.write(0,0,'商品名称')
Worksheet.write(0,1,'图片网站')
Worksheet.write(0,2,'详细信息')
Worksheet.write(0,3,'价格')
Worksheet.write(0,4,'发货地址')
for auction in auctions:
    if ('view_sales' in auction.keys()):
        raw_title = auction['raw_title']
        pic_url = auction['pic_url']
        detail_url = auction['detail_url']
        view_price = auction['view_price']
        item_loc = auction['item_loc']
        view_sales = auction['view_sales']
        print(raw_title,pic_url,detail_url,view_price,item_loc,view_sales)
        raw_title = auction['raw_title']
        Worksheet.write(i, 0, raw_title)
        i = i + 1
        pic_url = auction['pic_url']
        Worksheet.write(j, 1, pic_url)
        j = j + 1
        detail_url = auction['detail_url']
        Worksheet.write(k, 2, detail_url)
        k = k + 1
        view_price = auction['view_price']
        Worksheet.write(l, 3, view_price)
        l = l + 1
        item_loc = auction['item_loc']
        Worksheet.write(m, 4, item_loc)
        m = m + 1
        view_sales = auction['view_sales']
        Worksheet.write(n, 5, view_sales)
        n = n + 1
        time.sleep(random.random())
    else:
        raw_title = auction['raw_title']
        pic_url = auction['pic_url']
        detail_url = auction['detail_url']
        view_price = auction['view_price']
        item_loc = auction['item_loc']
        print(raw_title,pic_url,detail_url,view_price,item_loc)
        raw_title = auction['raw_title']
        Worksheet.write(i, 0, raw_title)
        i = i + 1
        pic_url = auction['pic_url']
        Worksheet.write(j, 1, pic_url)
        j = j + 1
        detail_url = auction['detail_url']
        Worksheet.write(k, 2, detail_url)
        k = k + 1
        view_price = auction['view_price']
        Worksheet.write(l, 3, view_price)
        l = l + 1
        item_loc = auction['item_loc']
        Worksheet.write(m, 4, item_loc)
        m = m + 1
        n = n + 1
        time.sleep(random.random())
Workbook.save('taobao.xls')"""
#Workbook.save('%s.xls'%(url))



#Worksheet.write(0,5,'付款人数')
'''for auction in auctions:
    raw_title=auction['raw_title']
    Worksheet.write(i, 0, raw_title)
    i=i+1
for auction in auctions:
    pic_url = auction['pic_url']
    Worksheet.write(j,1,pic_url)
    j=j+1
for auction in auctions:
    detail_url = auction['detail_url']
    Worksheet.write(k,2,detail_url)
    k=k+1
for auction in auctions:
    view_price = auction['view_price']
    Worksheet.write(l,3,view_price)
    l=l+1
for auction in auctions:
    item_loc = auction['item_loc']
    Worksheet.write(m,4,item_loc)
    m=m+1
for auction in auctions:
    view_sales = auction['view_sales']
    Worksheet.write(n,5,view_sales)
    n=n+1
Workbook.save('taobao.xls')

    #print(raw_title,pic_url,detail_url,view_price,item_loc,view_sales)
#print(response.text)
#print(json_str)
'''
