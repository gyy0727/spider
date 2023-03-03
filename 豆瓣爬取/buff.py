import requests	 #导入请求包
import re 	#正则

url = "http://e053db8f-1cff-4c06-971c-1ca161d3f2ec.node4.buuoj.cn:81/?name=1"
#添加User-Agent
params={
 'key': 'ctfisgood'
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.175.400 QQBrowser/11.1.5155.400',

    }
resp = requests.post(url, headers=headers) #获取响应数据
page_content = resp.text #提取源代码