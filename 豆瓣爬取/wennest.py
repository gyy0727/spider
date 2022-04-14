import requests
import re
import json
import xlwt
import time
import random
import xlrd

url='https://s.taobao.com/search?spm=a230r.1.0.0.2e9f46cbnaml6o&q=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&rs=up&rsclick=13&preq=%E5%86%85%E8%A1%A3'
headers={
'cookie': 'cna=AXSKGrr2wzcCAXBgUuTWQSfM; miid=540565579919513653; tracknick=tb762580637; enc=BJj9pKwQIrEiGXc4wgA3hE%2FAZDO7XL8usifyeKXGKwOPOH4jLnGjAANrqFJB3bhcz2TSgHGwuVoM97mItsg%2B75rIb5Rp9MNfH0fLZTzjUY4%3D; sgcookie=E100%2FZBUssj9my5IQZ5T9yCWM%2FAB9RaojX9HoUK99vtJD09VXNR4JctbRyXgnrRjEDhw8a83hbSq7YAHJoIpuArN2SZ0ypCXzge5Gb9UAn%2F3lAwAaDExT8w%2FGn5kj%2BlESRlm; uc3=vt3=F8dCvCtOrgxOs1hBR40%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&nk2=F5RCY8NEs3CyrtI%3D&id2=UUphyu7sTaoEuvCPDQ%3D%3D; csg=07bcd117; lgc=tb762580637; uc4=nk4=0%40FY4JjT4SZE8bMNT4zsdVErU%2BjQ0z%2Fw%3D%3D&id4=0%40U2grEago5Fif%2B4reQSSQROIFjZRh0Oxt; _cc_=UIHiLt3xSw%3D%3D; sg=719; thw=cn; mt=ci=-1_0; t=409765409df8dce5edb15348aa1e1b35; _m_h5_tk=8f22b5e3d041e6a0b6c43d9d04a06ff6_1649049622793; _m_h5_tk_enc=05a0dfb6a551ea226c779bc7daecb2f8; _tb_token_=eb5993e753eeb; isg=BGJi0ar6dPcXmGil5nnUeerjpujEs2bNBeUUwKz7jlWAfwL5lEO23eh9q7uD695l; uc1=cookie14=UoewCZQHtaNDzQ%3D%3D; tfstk=clpABAXUt400htsJYIhk5ZMd_Puhw04lP7QaB0mr4txWYa1DtpvLPnnRX9oI2; l=eBTmqI3RLYrU7bnLBOfanurza77OSLAYYuPzaNbMiOCP9QCB5KzlW6VZFW86C3GVhsMDR3rxuoN2BeYBq7VonxvtIosM_Ckmn; x5secdata=xbde5fb7af9587ec5099e505eb18e869561649041346a-717315356a1993109894abazc2aaa__bx__fourier.taobao.com%3A443%2Frp; xlly_s=1',
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
}
proxies = {
    'http': '27.206.137.9:8088',
}
response=requests.get(url=url,headers=headers,proxies=proxies)
time.sleep(random.random())
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
Worksheet=Workbook.add_sheet("wenxiong")
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
Workbook.save('wenxiong.xls')