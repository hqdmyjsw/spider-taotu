# -*- coding:utf-8 -*-

import time
import random
import sqlite3
import hashlib
import requests
import threading

#MD5加密函数
def hash_str(plain_str):
    md5 = hashlib.md5()
    md5.update(plain_str.encode('utf-8'))
    return md5.hexdigest()

def down_imgs(img_url):
    fname = "imgs/"+hash_str(img_url) + '.jpg'
    r = requests.get(img_url)
    with open(fname,"wb+") as f:
        f.write(r.content)

db = sqlite3.connect("spider_tt8.db",check_same_thread=False)
cur = db.cursor()
cur.execute("select urls from xiuren")
l = cur.fetchall()

for i in l:
    a = i[0]
    for ii in str(a).split(","):
        aa = ii.replace(" ","")
        if "http" in aa:
            try:
                t = "t" + str(random.randint(0,9999))
                t = threading.Thread(target=down_imgs, args=(aa, ))
                t.start()
                time.sleep(0.1)
                print("Success      "+str(hash_str(ii))+".jpg")
            except:
                pass