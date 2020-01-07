import re
import urllib

import requests
from lxml import etree

handers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
url = "http://www.cntour.cn"
page = urllib.request.urlopen(url)
html = page.read().decode('utf-8')
reg = r'<img src="(.+?\.png)"'#正则表达式
reg_img = re.compile(reg)#编译一下，运行更快
rej = r'<img src="(.+?\.jpg)"'#正则表达式
reg_imgj = re.compile(rej)#编译一下，运行更快
imglist=re.findall(reg_img ,html)
imglist+=re.findall(reg_imgj ,html)
count=1
for img in imglist:
    img_add =url+img
    f = open("G:\Python\photo\\" + str(count) + ".png", 'wb')
    img_html = urllib.request.urlopen(img_add)
    picture = img_html.read()
    # f.write(picture)
    # f.close()
    count += 1
    print(picture)