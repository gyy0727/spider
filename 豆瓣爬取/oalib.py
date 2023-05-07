import re
import warnings

import requests
import xlwt
import ssl
warnings.filterwarnings("ignore")

# 输出特定类型的警告
# 例如，禁止 DeprecationWarning：
warnings.filterwarnings("ignore", category=DeprecationWarning)
ssl._create_default_https_context = ssl._create_unverified_context

url2 = []
dataAll=[]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.205.400 QQBrowser/12.0.5435.400'

}


def searchPage():
    print("searchpage")
    kwyWordToSearch = "computer"
    toYear = "2023"
    fromYear = "2020"
    page = 1
    url1 = "http://www.oalib.com/search?type=0&oldType=0&kw=" + kwyWordToSearch + "&searchField=keyword&searchField=All&__multiselect_searchField=&fromYear=" + fromYear + "&toYear=" + toYear + "&pageNo=" + str(
        page)
    response = requests.get(url=url1, headers=headers,verify=False)
    res = response.text

    # print(res)
    resultNum=re.findall(r'Page\s.*?\s/(.*?)</div>',res,re.DOTALL)
    if len(resultNum)==0:
        resultNum=re.findall(r"第.*?页/共(.*?)条",res)
    pageNUM=re.findall(r"Page\s(.*?)\s/.*?\s</div>",res,re.DOTALL)
    if len(pageNUM) == 0:
        pageNUM=re.findall(r"第(.*?)页/共.*?条",res)


    # url2 = re.findall(r"<span style=\"font-size: 16px;\" ><a\s+href=\"//(.*)\"\starg", res)
    # print(resultNum)
    # print(pageNUM)
    #
    # print(url1)
    # print(url2)
    pageToSpider=int(resultNum[0])//10
    print("应有"+str(pageToSpider)+"页,请问想爬取多少页:")
    howMuchToSpider=input("请输入你想爬取的页数")
    howMuchToSpider=int(howMuchToSpider)+1
    for i in range(1,howMuchToSpider):
        print("-----------------共找到" + str(resultNum[0] )+ "篇论文" + "---------------当前爬取第" + str(i) + "页---------------------")
        around(i)

def around(str1):
    # print("around")
    kw = "computer"
    toyear = "2023"
    fromyear = "2020"
    page = 1
    url1 = "http://www.oalib.com/search?type=0&oldType=0&kw=" + kw + "&searchField=keyword&searchField=All&__multiselect_searchField=&fromYear=" + fromyear + "&toYear=" + toyear + "&pageNo=" + str(str1)
    response = requests.get(url=url1, headers=headers, verify=False)
    res = response.text

    # print(res)
    resultNum = re.findall(r'Page\s.*?\s/(.*?)</div>', res, re.DOTALL)
    if len(resultNum) == 0:
        resultNum = re.findall(r"第.*?页/共(.*?)条", res)
    pageNUM = re.findall(r"Page\s(.*?)\s/.*?\s</div>", res, re.DOTALL)
    if len(pageNUM) == 0:
        pageNUM = re.findall(r"第(.*?)页/共.*?条", res)

    url2 = re.findall(r"<span style=\"font-size: 16px;\" ><a\s+href=\"//(.*)\"\starg", res)
    # print(resultNum)
    # print(pageNUM)
    # print("-----------------共找到" + str(resultNum[0]) + "篇论文" + "---------------当前爬取第" + str(
    #     pageNUM[0]) + "页---------------------")
    # print(url1)
    # print(url2)
    data1 = 0
    for i in range(10):
        paper(url2[i], data1)
        print(url2[i])
    data1 += 1


def paper(url, data1):
    # print("paper")

    # 通过工作薄对象创建sheet,sheetName 要求长度小于31个字符，并且不能存在斜杠，否则会报错
    data = []
    response = requests.get(url="https://" + url, headers=headers,verify=False)
    if response.status_code == 200:
        res = response.text
        downurl = re.findall(r"<p class=\"doi\" style=\"line-height: 30px\"><a href=\"(.*)\"\ssty", res)
        # print("test")
        title = re.findall(r"<p\sstyle=\"border-bottom:.*both\">\s</p>\s*<h1>(.*)</h1>", res)
        author = re.findall(r"kw=.*?&searchField=authors\">(.*?)</a>", res)
        keyword = re.findall(r"kw=.*?&searchField=keyword\">(.*?)</a>", res)
        abstract = re.findall(r"<div\sstyle=\"line-height:21px;font-size:11pt\"><p>(.*)</p></div>\s</span>", res,re.DOTALL)
        year = re.findall(r"</a>&nbsp;(.*)&nbsp;</div>", res)
        strtitle = ""
        strauthor = ""
        strkeyword = ""
        stryear = ""
        if len(title)!=0:
            strtitle = title[0]

        if len(author) != 0:
            for str in author:
                strauthor = strauthor + str
            for str in keyword:
                strkeyword = strkeyword + str


        if len(year)!=0:
            stryear = year[0]

        # 首先需要在第0行写入表头，然后再写入后续数据，但是都是使用的write方法写入，只是坐标不一样


        data.append(stryear)
        data.append(strtitle)
        data.append(strauthor)
        data.append(strkeyword)
        if len(abstract) != 0:
            strabstract = abstract[0]
            data.append(strabstract)
        else:
            data.append("无")
        dataAll.append(data)
        # 循环写入表头
        # 循环写入数据
        # print(year)
        # # print(downurl)
        # print(title)
        # print(author)
        # print(keyword)
        # print(abstract)
        download(downurl[0], strtitle)
    else:
        print(url+"访问失败")



def saveExcel():
    workBook = xlwt.Workbook(encoding='utf-8')
    sheet = workBook.add_sheet("论文")
    head = ['发表年份', '论文题目', '作者', '论文关键词', '摘要']
    for i in range(5):
        sheet.write(0, i, head[i])
    for i in range(len(dataAll)):
        for j in range(len(dataAll[i])):
            sheet.write(i + 1, j, dataAll[i][j])
    savePath = '..\\paper\\test.xls'
    workBook.save(savePath)
    print("excel保存成功")

def main():
    print("main")
    searchPage()
    saveExcel()

    # 创建一个工作簿对象，设置编码格式为“utf-8”，默认格式是ASCII，为了方便写入中文，一般都要设置成UTF-8

    # 通过workBook对象的save方法保存文档,savePath可以是绝对路径，也可以是相对了路径




def download(url2,title):
    print("download")
    title = title.replace("<sub>", "_").replace("</sub>", "_")
    cleaned_filename = re.sub(r'[<>:"/\\|?*]', '_',title)
    url3 = url2
    response = requests.get(url=url3, headers=headers,verify=False)
    if response.status_code == 200:
        # 如果响应状态码为200，表示请求成功
        # 获取文件名，通常可以从URL中提取
        file_name = url3.split("/")[-1]

        # 以二进制模式写入文件
        with open("..\\paper\\"+cleaned_filename+ ".pdf", 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"PDF文件已成功下载为 {cleaned_filename}")
    else:
        print(f"下载失败，响应状态码为 {response.status_code}")


# res=response.text
# print(res)


if __name__ == "__main__":
    main()
