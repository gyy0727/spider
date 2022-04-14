from bs4 import BeautifulSoup
import lxml
import  requests

url="https://movie.douban.com/top250"
params={
 'start': '25',
 'filter': '50'
}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.96.400 QQBrowser/10.9.4619.400',
}
response = requests.get(url=url,params=params,headers=headers)
html=response.content
soup=BeautifulSoup(html,'lxml')
'''
print(soup.prettify())
'''
'''
for string in soup.stripped_strings:
  print(string)
'''

aas=soup.find_all('span')