# from selenium import webdriver
# from selenium.webdriver.common.proxy import ProxyType
# from twisted.protocols.portforward import Proxy
#
# firefox_binary = r"D:\firefox\Mozilla Firefox\firefox.exe"
#
# #
# # 创建Firefox WebDriver
# #
# #
# # 设置User-Agent
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
# firefox_options.set_preference("general.useragent.override", user_agent)
#
# #
# #
# # # 创建Firefox WebDriver并传递Profile
# #
# #
# #
# #
# # # 创建Firefox Profile
# #
# #
# # # 创建Firefox WebDriver并传递Profile
# driver = webdriver.Firefox(executable_path=r"C:\Users\mu'qiu\Desktop\request-test\venv\Scripts\geckodriver.exe",firefox_binary=firefox_binary,options=firefox_options)
# #
# # # 打开网页
# url = 'https://kns.cnki.net/kns8s/?classid=LSTPFY1C'
# driver.get(url)
# #
# # # 添加Cookie
# #
# # # 刷新页面以应用Cookie
# #
# a=driver.page_source
# # # 后续操作
# # # 您可以继续使用driver来执行其他操作，如查找元素、获取页面内容等
# #
# print(a)











import time

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from urllib.parse import urljoin


def open_page(driver, theme):
    # 打开页面
    driver.get("https://kns.cnki.net/kns8/AdvSearch")
    # 传入关键字
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '''//*[@id="gradetxt"]/dd[1]/div[2]/input'''))).send_keys(theme)
    # 点击搜索
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-search"))).click()
    time.sleep(3)

    # # 点击切换中文文献
    # WebDriverWait(driver, 100).until(
    #     EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div/div/div/a[1]"))).click()
    # time.sleep(3)
    # 获取总文献数和页数
    res_unm = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '''//*[@id="countPageDiv"]/span[1]/em'''))).text
    # 去除千分位里的逗号
    res_unm = int(res_unm.replace(",", ''))
    page_unm = int(res_unm / 20) + 1
    print(f"共找到 {res_unm} 条结果, {page_unm} 页。")
    return res_unm


def crawl(driver, papers_need, theme):
    with open(f'CNKI_{theme}.tsv', 'a', encoding='utf-8') as f:
        f.write(f"count\ttitle\tauthors\tinstitute\tdate\tsource\tdatabase\tkeywords\tabstract\turl".replace(
                        "\n", "") + "\n")

        # 赋值序号, 控制爬取的文章数量
        count = 1

        # 当爬取数量小于需求时，循环网页页码
        while count <= papers_need:
            # 等待加载完全，休眠3S
            time.sleep(3)

            title_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fz14")))
            # 循环网页一页中的条目
            for i in range(len(title_list)):
                try:
                    term = count % 20  # 本页的第几个条目

                    title_xpath = f"/html/body/div[3]/div[2]/div[2]/div[2]/form/div/table/tbody/tr[{term}]/td[2]"
                    author_xpath = f"/html/body/div[3]/div[2]/div[2]/div[2]/form/div/table/tbody/tr[{term}]/td[3]"
                    source_xpath = f"/html/body/div[3]/div[2]/div[2]/div[2]/form/div/table/tbody/tr[{term}]/td[4]"
                    date_xpath = f"/html/body/div[3]/div[2]/div[2]/div[2]/form/div/table/tbody/tr[{term}]/td[5]"
                    database_xpath = f"/html/body/div[3]/div[2]/div[2]/div[2]/form/div/table/tbody/tr[{term}]/td[6]"
                    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, title_xpath))).text
                    authors = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, author_xpath))).text
                    source = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, source_xpath))).text
                    date = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, date_xpath))).text
                    database = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, database_xpath))).text

                    # 点击条目
                    title_list[i].click()
                    # 获取driver的句柄
                    n = driver.window_handles
                    # driver切换至最新生产的页面
                    driver.switch_to.window(n[-1])
                    time.sleep(3)
                    # 开始获取页面信息



                    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,"/html/body/div[2]/div[1]/div[3]/div/div/div[3]/div/h1"))).text
                    authors = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,"/html/body/div[2]/div[1]/div[3]/div/div/div[3]/div/h3[1]"))).text
                    institute = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div/div[3]/div/h3[2]"))).text
                    abstract = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "abstract-text"))).text
                    try:
                        keywords = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "keywords"))).text[:-1]
                    except:
                        keywords = '无'
                    url = driver.current_url
                    time.sleep(10)
                    # 获取下载链接
                    link = driver.find_element_by_id("cajDown")
                    link.click()
                    time.sleep(10)
                    time.sleep(10)

                    link = WebDriverWait( driver, 10 ).until( EC.presence_of_all_elements_located((By.CLASS_NAME  ,"btn-dlcaj") ) )[0].get_attribute('href')
                    link = urljoin(driver.current_url, link)
                    print(link)

                    # 写入文件
                    res = f"{count}\t{title}\t{authors}\t{institute}\t{date}\t{source}\t{database}\t{keywords}\t{abstract}\t{url}".replace(
                        "\n", "") + "\n"
                    print(res)
                    f.write(res)


                except:
                    print(f" 第{count} 条爬取失败\n")
                    # 跳过本条，接着下一个
                    continue
                finally:
                    # 如果有多个窗口，关闭第二个窗口， 切换回主页
                    n2 = driver.window_handles
                    if len(n2) > 1:
                        driver.close()
                        driver.switch_to.window(n2[0])
                    # 计数,判断需求是否足够
                    count += 1
                    if count == papers_need: break

            # 切换到下一页
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='PageNext']"))).click()



if __name__ == "__main__":
    # get直接返回，不再等待界面加载完成
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"

    # 设置谷歌驱动器的环境
    options = webdriver.EdgeOptions()
    # 设置chrome不加载图片，提高速度
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # # 设置不显示窗口
    # options.add_argument('--headless')
    # 创建一个谷歌驱动器
    driver = webdriver.Edge(options=options)
    # 设置搜索主题
    theme = "社会"
    # 设置所需篇数
    papers_need = 5

    res_unm = int(open_page(driver, theme))
    #判断所需是否大于总篇数
    papers_need = papers_need if (papers_need <= res_unm) else res_unm

    crawl(driver, res_unm, theme)

    # 关闭浏览器
    driver.close()