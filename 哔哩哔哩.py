import requests
from selenium import webdriver
import  re

browser = webdriver.Chrome()
browser.get(url='https://www.classviva.org/mod/quiz/attempt.php?attempt=2513709&cmid=17285')
res=browser.page_source
print(res)
browser.close()