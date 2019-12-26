# -*- coding:utf-8 -*-

'''
cursor.execute('insert into words (id, word, mean) values (?, ?, ?)', (i, word_a, mean_a))
# 或者
cursor.execute('insert into words (id, word, mean) values (:id, :word, :mean)', {"id": i, "word": word_a, "mean": mean_a})
'''

import sqlite3

db = sqlite3.connect("spider_tt8.db",check_same_thread=False)
cur = db.cursor()

#创建数据表
def found_db(dbname):
    #SQL语句，创建一个表，用来储存 编号id,图片名字name，标签tags，链接urls
    sql1 = """CREATE TABLE %s( 
         id  INT,
         name  TEXT,
         tags TEXT,
         urls TEXT,
         sha  TEXT)""" % \
         (dbname,)

    #执行SQL语句
    cur.execute(sql1)
    #插入第一行数据作为参考
    insert_data(dbname," ",' ',' ',' ',1,tid=1)

#向已有的表中插入数据
#insert_data("abc1",2,"name","tags","urls","sha1")
def insert_data(tname,str2,str3,str4,str5,str1=0,tid=None):
    if tid is None:
        #将查询到的最大ID + 1 ，自动补全ID
        sql_max_id = "select max(id) from %s" %tname
        cur.execute(sql_max_id)
        str1 = cur.fetchone()[0] + 1

    #插入相关数据
    sql2 = "INSERT INTO %s (id, \
            name, tags, urls,sha) \
            VALUES ('%d', '%s',  '%s',  '%s',  '%s' )" % \
            (tname,str1,str2,str3,str4,str5)
    #执行数据库更新命令
    cur.execute(sql2)
    db.commit()




