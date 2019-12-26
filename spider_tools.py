# -*- coding: UTF-8 -*-
import re
import time
import random
import hashlib
import requests
import threading
from lxml import etree

td8_url = "https://www.192td.com"

#定制一个请求头，伪造真实用户
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

#MD5加密函数
def hash_str(plain_str):
    md5 = hashlib.md5()
    md5.update(plain_str.encode('utf-8'))
    return md5.hexdigest()

#类
class PageSpider(object): 
    def __init__(self,para_url=None):
        if para_url != None:
            self.url = para_url
            self.res = requests.get(para_url,headers=headers)
            self.res.encoding = "utf-8"
            self.soup = etree.HTML(self.res.text)

    #用来解析总的封面页面数量
    def page_sum(self):
        temp_page_sum = self.soup.xpath("//div[@class='page']/a/@href")
        page_sum = len(temp_page_sum)
        page_str = temp_page_sum[page_sum-1]
        x = int(re.compile(r'index_(.*).html').findall(page_str)[0])
        url_1 = re.compile(r'https.*.x').findall(self.url)[0]
        #print(self.url)
        #定义一个空的数组
        list1 = []
        list1.append(self.url)
        for i in range(2,x+1):
            #向数组中添加新的数据
            list1.append(url_1+"_"+str(i)+'.html')
        return list1

    #将封面页面的链接解析出来
    def page_list(self,url1):
        #创建一个列表用于保存详细链接
        detail_info_url = []
        self.soup = PageSpider(url1).soup
        page_lists = self.soup.xpath("//ul[@class='clearfix']/li/a/@href")
        for page in page_lists:
            if "https" in page:
                detail_info_url.append(page)
            else:
                detail_info_url.append(td8_url+page)
        return detail_info_url

    #抓取页面总数page—allnum，以及详细信息
    def page_data(self,page_url):
        self.soup = PageSpider(page_url).soup
        #创建一个列表，用于储存每一个详情页面的详情信息
        list_page_data = []

        '''
        list_page_data[0] : 储存标题
        list_page_data[1] : 储存页面标签
        list_page_data[2:len(list_page_data)] : 储存详情页面链接地址
        '''
        
        try:
            page_allnum = int(self.soup.xpath("//span[@id='allnum']/text()")[0])
            items_title = self.soup.xpath("//div[@class='breadnav']/a[4]/text()")[0]
            items_tags = self.soup.xpath("//div[@class='picbottomline']/p/span/a/text()")
            list_page_data.append(items_title) #将页面标题 加入列表
            list_page_data.append(items_tags) #将页面标签列表加入列表
            list_page_data.append(page_url) #将传入页面加入页面地址
            #过滤干扰字符
            if '+' in items_tags:
                del items_tags[-3:-1]
                items_tags.remove('+')

            url_1 = re.compile(r'https.*[0-9]').findall(page_url)[0]
            for page_num in range(2,page_allnum+1):
                page_num_url = url_1+'_'+str(page_num)+'.html'
                list_page_data.append(page_num_url)

        except:
            print("抓取页面： "+page_url+'   页面详情时出现了一个错误！')
    
        return list_page_data
     
    #抓取图片地址信息
    def page_img(self,page_url):
        self.soup = PageSpider(page_url).soup
        try:
            items_img = self.soup.xpath("//div[@class='picsbox picsboxcenter']/center/img/@lazysrc")[0]
        except:
            print("抓取页面： "+page_url+"   图片地址时，出现了一个致命错误！")
        return items_img

    #传入一个待抓取的详情页面，返回页面的 标题，标签（列表），图片地址（列表）
    def all_data(self,pages):
        #创建一个列表，储存最终所有信息
        all_data = []
        '''
        all_data[0] 标题
        all_data[1] 标签
        all_data[2] 地址
        '''
        #创建一个列表，储存地址合集
        img_urls = []
        
        a = PageSpider().page_data(pages)
        all_data.append(a[0])   #添加标题
        all_data.append(a[1])   #添加标签

        #设置一个添加元素的函数
        def add_url(a):
            img_urls.append(a)
        
        for i in a[2:len(a)]:
            try:
                #为线程对象产生不同名称
                x = str(random.randint(0,100))
                t = 't' + x
                t = threading.Thread(target=add_url, args=(PageSpider().page_img(i),))
                t.start()
                #延时0.3秒防止请求过快
                time.sleep(0.2)
                #img_urls.append(PageSpider().page_img(i)) #将解析出的图片地址添加进去
            except:
                print("执行线程"+x+"时，出现了一个错误！")
        all_data.append(img_urls) #添加地址组

        return all_data