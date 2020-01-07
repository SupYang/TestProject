"""p=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j)and (i!=k)and(j!=k):
                print(i,j,k)
                p=p+1

print(p)
"""
"""
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print ((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)
"""
"""
count=[45,67,32,11,9,99,82,43,55,7,76]
#print(len(count))
for i in range(len(count)):
    for j in range(0,len(count)-i-1):
        if count[j]>count[j+1]:
            count[j],count[j+1]=count[j+1],count[j]

for o in range(len(count)):
    print(count[o])
    """
"""
Y=int(input('请输入年:\n'))
M=int(input('请输入月份:\n'))
D=int(input('请输入天:\n'))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0<M<=12:
    sun=months[M-1]
else:

    print('月份输入错误')
    exit(1)
sun+=D
leap=0
if(Y%400==0)or((Y%100!=0) and(Y%4==0)):
    leap=1
if(leap==1)and(M>2):
    sun+=1
print('共：%d天' %sun)

n=int(input('请输入：'))
a,b=1,1
if (n!=0) and (n!=1):
    for i in range(n-1):
        a,b,=b,a+b
        print(a)
else:
    print(0)
   
def Getf(n):
    if n==1 or n==2:
        return 1
    return Getf(n-1)+Getf(n-2)
print(Getf(10))

def Getl(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fbs=[1,1]
    for i in range(2,n):
        fbs.append(fbs[-1]+fbs[-2])
    return fbs
print(Getl(10))

for i in range(1, 10):
    print('0')
    for j in range(1,i+1):
        print('%d*%d=%d' % (j,i,i*j),end=" ")
 
for i in range(5):
    for j in range(6):
        print('*',end=" ")
    print()

for i in range(4):
    for j in range(4):
        if i==0 or i==3:
            print('*',end="  ")
        elif j==0 or j==3:
            print('&',end="  ")
        else:
            print(" ",end="  ")
    print()

 


# for i in range(1,6):
#     for o in range(1,6-1):
#        print(' ',end='')
#     print(' * '*i)

for i in range(1, 6):
        for j in range(1, 6 - i):
            print("1", end=" ")
        for k in range(1, i + 1):
            print(" * ", end=" ")
        print(" ")


open("G://Python//test.txt","wt").write("55555\r\n55555")
txt=open("G://Python//test.txt","rt").read()
print(txt)

import datetime
print(datetime.timedelta(days=1))


import re
import urllib.request
url='https://vacations.ctrip.com/list/whole/d-lijiang-32.html?salecity=28#ctm_ref=hp_tour_pt_pro_01'
yuan=urllib.request.urlopen(url)
txt=yuan.read()
title = r'src="(.+?\.jpg)"'#正则表达式
tt = re.compile(title)
titlelist=re.findall(tt ,txt.decode('utf-8'))
x=0
for t in titlelist:
        open("G://Python//test.txt","a").write(t)
        x += 1
"""

import requests
from lxml import etree
import cx_Oracle
# 更新游戏列表
conn = cx_Oracle.connect('CD3_GZNS_CUST', 'CD3_GZNS_CUST', '192.168.100.107/ORCL')
cursor = conn.cursor()
heads = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",'content-type':'text/html; charset=gb2312'}
# 需要爬取的游戏列表页
url = 'https://www.ctrip.com/'
# 不压缩html，最大链接时间为10妙
res = requests.get(url,headers=heads)
# 为防止出错，编码utf-8
res.encoding = 'gb2312'
print(res.content)
# 将html构建为Xpath模式
root = etree.HTML(res.content)
#print("root+"% root)
# 使用Xpath语法，获取游戏名
gameList = root.xpath("//ul[@class='departures_sequence']//li//a[1]//text()")
print(res.status_code)
print(gameList)
# 输出爬到的游戏名
x=0
for img in gameList:
    print(gameList[x])
    yy = "insert into AAAAA（QS,MD,RE) values('{}','{}','--')".format(gameList[x],gameList[x+1])
    print(yy)
    result=cursor.execute(yy)

    conn.commit()

    x += 2
print(x)
cursor.close()
conn.close()
"""
import requests
import cx_Oracle
from bs4 import BeautifulSoup
import re   # 在python中调用正则表达式用re库，这个库不用安装，可直接调用
conn = cx_Oracle.connect('CD3_GZNS_CUST', 'CD3_GZNS_CUST', '192.168.100.107/ORCL')
cursor = conn.cursor()
url = 'https://www.ctrip.com/'
handers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
strhtml = requests.get(url,headers=handers)  # 所有在源码中的数据请求方式都是get
soup = BeautifulSoup(strhtml.text, 'lxml') # lxml解析器进行解析，解析之后的文档保存到变量soup
#print(soup)
# 使用soup.select引用这个路径
data = soup.select('ul.departures_sequence>li>a')
print(data)
# 清洗和组织数据，完成上面的步骤只是获得了一段目标HTML代码，但没有把数据提取出来

#for item in data:                    # soup匹配到的有多个数据，用for循环取出

    #result = {
       #'title': item.get_text().replace(' ','').replace('		',''),     # 标签在<a>标签中，提取标签的正文用get_text()方法
        #'link': item.get('href'),  # 链接在<a>标签的href中，提取标签中的href属性用get()方法，括号指定属性数据
        #'ID': re.findall('\d+', item.get('href'))    # 每一篇文章的链接都有一个数字ID。可以用正则表达式提取这个ID;\d  匹配数字； + 匹配前一个字符1次或者多次
    #}
    #tt=item.get_text().replace(' ','').replace('	','')

    #print(tt[0:10])
    #for a in result:
        #yy = "insert into AAAAA（QS,MD,RE,RE1) values('%d','%d','%d','%d')" % tt[3:5], tt[8:10], tt[6:7], tt[0:3]
        #print('%d' % tt)
        #result=cursor.execute(yy)
#all_data=result.fetchall()
#for item in all_data:


cursor.close()
conn.commit()
conn.close()

"""