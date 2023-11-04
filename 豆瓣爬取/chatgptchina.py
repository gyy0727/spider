import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
movies_list = soup.find_all('div', class_='hd')

for i, movie in enumerate(movies_list):
    movie_name = movie.a.span.text.strip()
    print(f'{i+1}. {movie_name}')