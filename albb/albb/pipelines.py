# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import MySQLdb
class AlbbPipeline(object):
    j=1
    Conn= MySQLdb.connect(user='root', passwd='pwqagwt',
                              host='',db='maizi4',port=3306,charset="utf8")
    cur =Conn.cursor()
    cur.execute( "CREATE TABLE if not exists shopurl1( url VARCHAR(250)primary key,name VARCHAR(250))charset='utf8'")
    cur.execute( "CREATE TABLE if not exists Goodsinfo1( productname VARCHAR(250)primary key,shopurl VARCHAR(250),productkeyword1 VARCHAR(100),productkeyword2 VARCHAR(100),productkeyword3 VARCHAR(100))charset='utf8'")
    # cur.execute( "CREATE TABLE if not exists albb5( productname VARCHAR(250))charset='utf8'")
    Conn.commit()
    print 'sucess'
    def process_item(self, item, spider):
        self.j+=1
        sql = ("insert into shopurl(url,name) "
            "values(%s,%s)")
        sql1 = ("insert into Goodsinfo(productname,shopurl,productkeyword1,productkeyword2,productkeyword3) "
            "values(%s,%s,%s,%s,%s)")
        # sql1 = ("insert into albb5(productname) "
        #     "values(%s)")

        lis = (item['url'],item['name']
)
        lis1 = (item['product_name'],item['url'],item['product_key1'],item['product_key2'],item['product_key3'])       # lis1 = (item['product_name'].encode('gbk'))
        try:
             self.cur.execute(sql,lis)
        except Exception,e:
            # print "Insert error:",e
            self.Conn.rollback()
        try:

             self.cur.execute(sql1,lis1)


        except Exception,e:
            print "aaaInsert error:",e
            self.Conn.rollback()

        self.Conn.commit()
        print self.j
        # self.cur.close()
        # self.Conn.close()
        return item

