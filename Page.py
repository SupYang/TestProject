import requests
from lxml import etree


for i in range (1,4):
    handers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    url="http://www.cntour.cn/news/list.aspx?tid=54&page={}".format(i)
    data=requests.get(url,headers=handers).text
    html=etree.HTML(data)
    lu=html.xpath("//*[@class='newsList']//ul")
    for title in lu:
        tname=title.xpath(".//li//a//text()")
        for bb in tname:
        # tdate=title.xpath(".//li//text()")
            print(bb)