# -*- coding:utf-8 -*-

import time
import random
import threading
from spider_sql import found_db,insert_data
from spider_tools import PageSpider,hash_str

start_urls = "https://www.192td.com/gq/xiuren/index_2.html"

#定义表名称
db_name = 'xiuren'

#list 转 str 并 去除两端[]
def lts(str1):
    return str(str1).lstrip("[").rstrip("]").replace("'","")

#将列表中元素替换为sha1后的元素
def list_sha1(plainlist):
    list_data = []
    for para_url in plainlist:
        para_url = hash_str(para_url) + ".jpg"
        list_data.append(para_url)
    return list_data

found_db(db_name)

#将数据整理加密插入数据库
def enter_db(pdata):
    pdata.append(list_sha1(pdata[2]))
    insert_data(db_name,pdata[0],lts(pdata[1]),lts(pdata[2]),lts(pdata[3]))
    print("Success："+pdata[0]+"   已经成功插入数据库："+db_name)

#封装一下插入数据函数
def finn(param):
    enter_db(PageSpider().all_data(param)) 


a = PageSpider("https://www.192td.com/gq/xiuren/index.html").page_sum()
for i in a:
    b = PageSpider().page_list(i)
    it = iter(b)
    for ii in it:
        t = "te" + str(random.randint(0,99)) 
        t = threading.Thread(target=finn, args=(ii,))
        t.start()
        time.sleep(10)



