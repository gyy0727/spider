import requests
import re
import time
import random

url='https://search.jd.com/Search?keyword=%E7%94%B7%E8%A3%85&enc=utf-8&wq=%E7%94%B7%E8%A3%85&pvid=b5cf5efc5c7246eea380ce52180f5958'
header={
'cookie': 'cna=AXSKGrr2wzcCAXBgUuTWQSfM; miid=540565579919513653; tracknick=tb762580637; enc=BJj9pKwQIrEiGXc4wgA3hE%2FAZDO7XL8usifyeKXGKwOPOH4jLnGjAANrqFJB3bhcz2TSgHGwuVoM97mItsg%2B75rIb5Rp9MNfH0fLZTzjUY4%3D; lgc=tb762580637; _cc_=UIHiLt3xSw%3D%3D; sg=719; thw=cn; t=fb8b77c12390c9579494062c69ee4653; _m_h5_tk=f1b83ca2be23a6d08943a75da8ba75a1_1649250719594; _m_h5_tk_enc=7ee08bf72807827d9bac146753e33662; cookie2=1cac71b6c8d9eb9f4a1270099f52d514; _tb_token_=eee4761167637; xlly_s=1; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _samesite_flag_=true; sgcookie=E100i5nI%2Bpk5JoozNCvGbeztHWMFk3qI91Of2jG50dgq%2BvR2Eg7rZOV6L7cNQA0kGtT0%2F4Cxx1uEZoc6q48ShTYqvifZQpoL%2FVKmpOObbkcY6a1fbePvKIcxgKhaDwP6THqa; unb=2200777622471; uc3=vt3=F8dCvCtEwH8318Y%2Fq9w%3D&nk2=F5RCY8NEs3CyrtI%3D&id2=UUphyu7sTaoEuvCPDQ%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; csg=eb96eb8f; cancelledSubSites=empty; cookie17=UUphyu7sTaoEuvCPDQ%3D%3D; dnk=tb762580637; skt=27facdf4a1e58446; existShop=MTY0OTI0MjM5Mw%3D%3D; uc4=nk4=0%40FY4JjT4SZE8bMNT4zsdVE%2FAdm7lVZg%3D%3D&id4=0%40U2grEago5Fif%2B4reQSSQROIEy7TxQTyf; _l_g_=Ug%3D%3D; _nk_=tb762580637; cookie1=AiPJvIK9r9DPgXdTD7b1l0lpxBTbLojktc6XK8B6W78%3D; mt=ci=6_1; v=0; uc1=cookie14=UoewCZZ9Scxn5A%3D%3D&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0; JSESSIONID=FAA0B3C0D0DBE198F05FEC882BE0F2D4; isg=BPv7j1s3HU-P4CHy5_qtlltwn99lUA9SFDadN-241_oRTBsudCCfohkOY-wC2WdK; l=eBTmqI3RLYrU7YwCBOfanurza77OSLAvSuPzaNbMiOCPOUfp5BYPW6VISFT9CnhVhsCWJ3rxuoN2BeYBqo44n5U62j-la_kmn; tfstk=cq4lBFNOUuoScbm0fag7gIKMuFjAZbbjIR27uPp19U1iBvUViJt2bD6l4Y7sjH1..,',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.96.400 QQBrowser/10.9.4619.400'
}
proxies = {
    'http': '27.206.137.9:8088',
}
response=requests.get(url=url,headers=header,proxies=proxies)
time.sleep(random.random())
print(response.text)
