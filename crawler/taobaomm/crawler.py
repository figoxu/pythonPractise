#!/usr/bin/env python3

import os
import threading
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

browserPath = '/Users/xujianhui/develop/env/phantomjs-2.1.1-macosx/bin/phantomjs'
homePage = 'https://mm.taobao.com/search_tstar_model.htm?'
outputDir = 'photo/'
parser = 'html5lib'

def main():
    driver = webdriver.PhantomJS(executable_path=browserPath)  #浏览器的地址
    driver.get(homePage)  #访问目标网页地址
    bsObj = BeautifulSoup(driver.page_source, parser)  #解析目标网页的 Html 源码
    print("[*]OK GET Page")
    girlsList = driver.find_element_by_id('J_GirlsList').text.split(
        '\n')  #获得主页上所有妹子的姓名、所在城市、身高、体重等信息
    imagesUrl = re.findall('\/\/gtd\.alicdn\.com\/sns_logo.*\.jpg',
                           driver.page_source)  #获取所有妹子的封面图片
    girlsUrl = bsObj.find_all(
        "a",
        {"href": re.compile("\/\/.*\.htm\?(userId=)\d*")})  #解析出妹子的个人主页地址等信息
    # 所有妹子的名字地点
    girlsNL = girlsList[::3]
    # 所有妹子的身高体重
    girlsHW = girlsList[1::3]
    # 所有妹子的个人主页地址
    girlsHURL = [('http:' + i['href']) for i in girlsUrl]
    # 所有妹子的封面图片地址
    girlsPhotoURL = [('https:' + i) for i in imagesUrl]

    girlsInfo = zip(girlsNL, girlsHW, girlsHURL, girlsPhotoURL)

    # 姓名地址      girlNL，  身高体重 girlHW
    # 个人主页地址  girlHRUL, 封面图片 URL
    for girlNL, girlHW, girlHURL, girlCover in girlsInfo:
        print("[*]Girl :", girlNL, girlHW)
        # 为妹子建立文件夹
        mkdir(outputDir + girlNL)
        print("    [*]saving...")
        # 获取妹子封面图片
        data = urlopen(girlCover).read()
        with open(outputDir + girlNL + '/cover.jpg', 'wb') as f:
            f.write(data)
        print("    [+]Loading Cover... ")
        # 获取妹子个人主页中的图片
        getImgs(girlHURL, outputDir + girlNL)
    driver.close()


def mkdir(path):
    # 判断路径是否存在
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print("    [*]新建了文件夹", path)
        # 创建目录操作函数
        os.makedirs(path)
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print('    [+]文件夹', path, '已创建')


def getImgs(url, path):
    url = url.replace('http:','https:')
    print("  @url:",url,"  @path:",path," @browserPath:",browserPath)
    ua = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.3 Safari/537.36"
    cap = webdriver.DesiredCapabilities.PHANTOMJS
    cap["phantomjs.page.settings.resourceTimeout"] = 200000
    cap["phantomjs.page.settings.loadImages"] = True
    cap["phantomjs.page.settings.disk-cache"] = True
    cap["phantomjs.page.settings.userAgent"] = ua
    cap["phantomjs.page.customHeaders.User-Agent"] =ua
    driver = webdriver.PhantomJS(executable_path=browserPath,desired_capabilities=cap, service_args=['--ignore-ssl-errors=true'])
    print("Ready")
    driver.get(url)
    print("    [*]Opening...")
    bsObj = BeautifulSoup(driver.page_source, parser)
    #获得模特个人页面上的艺术照地址
    imgs = bsObj.find_all("img", {"src": re.compile(".*\.jpg")})
    for i, img in enumerate(imgs[1:]):  #不包含与封面图片一样的头像
        try:
            print("tryToDownload....", img['src'])
            html = urlopen('https:' + img['src'])
            data = html.read()
            fileName = "{}/{}.jpg".format(path, i + 1)
            print("    [+]Loading...", fileName)
            with open(fileName, 'wb') as f:
                f.write(data)
        except Exception:
            print("    [!]Address Error!")
    driver.close()


if __name__ == '__main__':
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    main()
