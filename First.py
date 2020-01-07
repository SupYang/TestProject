# coding:utf-8
import re
import urllib.request


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
a='Halo_World'
#print (get_html('http://tieba.baidu.com/p/1753935195'))

#
#
# reg = r'src="(.+?\.jpg)" width'#正则表达式
# reg_img = re.compile(r'src="(.+?\.jpg)" ')#编译一下，运行更快
# print(reg_img)
# imglist=re.findall(reg_img ,get_html('http://tieba.baidu.com/p/1753935195').decode('utf-8'))
#
# x=0
# for img in imglist:
#     urllib.request.urlretrieve(img, 'G:\Python\Img\%s.jpg' % x)
#     x += 1


def Get_Img(url):
    reg = r'src="(.+?\.jpg)" '#正则表达式
    reg_img = re.compile(reg)#编译一下，运行更快
    imglist=re.findall(reg_img ,url.decode('utf-8'))
    x=0
    for img in imglist:
        if img.find(u'https:')==-1:
         img='https:'+img
        urllib.request.urlretrieve(img, 'G:\Python\Img\%s.jpg' % x)
        print(img)
        x += 1

print(u'-------网页图片抓取-------')
print (u'请输入url:'),
url = input()
if url:
    pass
else:
    print(u'---没有地址输入正在使用默认地址---')
    url = 'http://tieba.baidu.com/p/1753935195'
print(u'----------正在获取网页---------')
html_code = get_html(url)
print(u'----------正在下载图片---------')

Get_Img(html_code)
print(u'-----------下载成功-----------')
input('Press Enter to exit')
