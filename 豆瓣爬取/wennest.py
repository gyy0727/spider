import requests
import json
import re
import time
import datetime


url='http://222.200.122.247:7780/'
headers={
'cookie': 'ASP.NET_SessionId=y4qjit45stn3w3q55pdsd345',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

}
proxies = {
    'http': '10.20.199.28:8080',
}
response=requests.get(url=url,headers=headers,proxies=proxies)

# time.sleep(random.random())
print(response.text)
# json_str=re.findall(r'g_page_config = (.*);',response.text)[0]
# json_dict=json.loads(json_str)
# #print(json_str)
# auctions=json_dict['mods']['itemlist']['data']['auctions']
# i=1
# j=1
# k=1
# l=1
# m=1
# n=1
# Workbook=xlwt.Workbook(encoding='utf-8')
# Worksheet=Workbook.add_sheet("wenxiong")
# Worksheet.write(0,0,'商品名称')
# Worksheet.write(0,1,'图片网站')
# Worksheet.write(0,2,'详细信息')
# Worksheet.write(0,3,'价格')
# Worksheet.write(0,4,'发货地址')
# for auction in auctions:
#     if ('view_sales' in auction.keys()):
#         raw_title = auction['raw_title']
#         pic_url = auction['pic_url']
#         detail_url = auction['detail_url']
#         view_price = auction['view_price']
#         item_loc = auction['item_loc']
#         view_sales = auction['view_sales']
#         print(raw_title,pic_url,detail_url,view_price,item_loc,view_sales)
#         raw_title = auction['raw_title']
#         Worksheet.write(i, 0, raw_title)
#         i = i + 1
#         pic_url = auction['pic_url']
#         Worksheet.write(j, 1, pic_url)
#         j = j + 1
#         detail_url = auction['detail_url']
#         Worksheet.write(k, 2, detail_url)
#         k = k + 1
#         view_price = auction['view_price']
#         Worksheet.write(l, 3, view_price)
#         l = l + 1
#         item_loc = auction['item_loc']
#         Worksheet.write(m, 4, item_loc)
#         m = m + 1
#         view_sales = auction['view_sales']
#         Worksheet.write(n, 5, view_sales)
#         n = n + 1
#         time.sleep(random.random())
#     else:
#         raw_title = auction['raw_title']
#         pic_url = auction['pic_url']
#         detail_url = auction['detail_url']
#         view_price = auction['view_price']
#         item_loc = auction['item_loc']
#         print(raw_title,pic_url,detail_url,view_price,item_loc)
#         raw_title = auction['raw_title']
#         Worksheet.write(i, 0, raw_title)
#         i = i + 1
#         pic_url = auction['pic_url']
#         Worksheet.write(j, 1, pic_url)
#         j = j + 1
#         detail_url = auction['detail_url']
#         Worksheet.write(k, 2, detail_url)
#         k = k + 1
#         view_price = auction['view_price']
#         Worksheet.write(l, 3, view_price)
#         l = l + 1
#         item_loc = auction['item_loc']
#         Worksheet.write(m, 4, item_loc)
#         m = m + 1
#         n = n + 1
#         time.sleep(random.random())
# Workbook.save('wenxiong.xls')




####
# -*- coding = utf-8 -*-

import requests
import json
import re
import time
import datetime

#
# def main():
#     session, header = login()
#
#
#
# # 用于验证登录是否成功
# def verify_login(url):
#     order_page = ''
#     if url == order_page:
#         print('登录成功')
#     else:
#         print('登录失败')
#
#
# # 该登录函数利用客户端的cookie信息完成登录，首次使用需要手动登录并获取cookie
# def login(cookies=None):
#     session = requests.session()
#     if cookies is None:
#         cookies = 'ASP.NET_SessionId=y4qjit45stn3w3q55pdsd345' # 这里是cookies
#
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
#         'Connection': 'keep-alive',
#         'Cookie': cookies
#     }
#     order_page = 'http://222.200.122.247:7780/'  # 这里是预约系统的URl地址
#     res = session.get(url=order_page, headers=header)
#     verify_login(res.url)
#     return session, header
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     main()

