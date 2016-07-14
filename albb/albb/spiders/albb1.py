
# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from albb.items import AlbbItem
import time
import urllib2
import re
import MySQLdb
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding("utf8")

class AlbbSpider(scrapy.Spider):
    name = "albb"
    urlset=set()
    allowed_domains = ["alibaba.com.com"]
    s1=time.time()
    # Conn= MySQLdb.connect(user='root', passwd='pwqagwt',
    #                           host='',db='maizi4',port=3306,charset="utf8")
    # cur =Conn.cursor()
    # cur.execute( "select*from albb11")
    # rs=cur.fetchall()
    # for i in rs:
    #     urlset.add(i[0])
    # print u'共取出'+ str(len(urlset)) +u'个'
    start_urls = (
        #"http://www.alibaba.com/catalogs/products/CID100003238?spm=a2700.7848340.1998821658.13.6ok5j5",
        'http://www.alibaba.com/catalogs/products/CID100005071?spm=a2700.7848340.1998821658.71.Kiy6Re',
        'http://www.alibaba.com/catalogs/products/CID711001?spm=a2700.7848340.1998821658.72.yYLwOU',
        'http://www.alibaba.com/catalogs/products/CID70802?spm=a2700.7848340.1998821658.73.4frCkB',
        'http://www.alibaba.com/catalogs/products/CID702?spm=a2700.7848340.1998821658.74.m0UbTU',
        'http://www.alibaba.com/catalogs/products/CID70804?spm=a2700.7848340.1998821658.75.Z4AGul',
        'http://www.alibaba.com/catalogs/products/CID708045?spm=a2700.7848340.1998821658.76.vas1o9'
        'http://www.alibaba.com/catalogs/products/CID100005062?spm=a2700.7848340.1998821658.77.xqqeBJ',
        'http://www.alibaba.com/catalogs/products/CID711005?spm=a2700.7848340.1998821658.78.5PugFZ',
        'http://www.alibaba.com/catalogs/products/CID100000050?spm=a2700.7848340.1998821658.88.w7cT6e',
        'http://www.alibaba.com/catalogs/products/CID100000013?spm=a2700.7848340.1998821658.89.L8QuEZ',
        'http://www.alibaba.com/catalogs/products/CID100000011?spm=a2700.7848340.1998821658.90.u6Ucvu',
        'http://www.alibaba.com/catalogs/products/CID100000026?spm=a2700.7848340.1998821658.91.50iUL4',
        'http://www.alibaba.com/catalogs/products/CID100000026?spm=a2700.7848340.1998821658.91.qb0amU',
        'http://www.alibaba.com/catalogs/products/CID100000054?spm=a2700.7848340.1998821658.92.ywLlbE',
        'http://www.alibaba.com/catalogs/products/CID100000014?spm=a2700.7848340.1998821658.93.wG1f4B',
        'http://www.alibaba.com/catalogs/products/CID100000014?spm=a2700.7848340.1998821658.93.rwPE5C',
        'http://www.alibaba.com/catalogs/products/CID100009632?spm=a2700.7848340.1998821658.81.TT1M6v',
        'http://www.alibaba.com/catalogs/products/CID100009630?spm=a2700.7848340.1998821658.82.vJrymN',
        'http://www.alibaba.com/catalogs/products/CID100009629?spm=a2700.7848340.1998821658.83.V6gQAQ',
        'http://www.alibaba.com/catalogs/products/CID100002954?spm=a2700.7848340.1998821658.84.pscY1M',
        'http://www.alibaba.com/catalogs/products/CID100002954?spm=a2700.7848340.1998821658.84.pWkzmP',
        'http://www.alibaba.com/catalogs/products/CID100009628?spm=a2700.7848340.1998821658.85.tWTpm1',
        'http://www.alibaba.com/catalogs/products/CID3011?spm=a2700.7848340.1998821658.96.u2aRm6',
        'http://www.alibaba.com/catalogs/products/CID3030?spm=a2700.7848340.1998821658.97.ZJBNGX',

        'http://www.alibaba.com/catalogs/products/CID3010?spm=a2700.7848340.1998821658.98.EPRCJi',
        'http://www.alibaba.com/catalogs/products/CID3005?spm=a2700.7848340.1998821658.99.PK3jvx',
        'http://www.alibaba.com/catalogs/products/CID3015?spm=a2700.7848340.1998821658.100.uhVsEy',

        'http://www.alibaba.com/catalogs/products/CID3019?spm=a2700.7848340.1998821658.101.8L353A',
        #HOSIERY
    )
    i,j,w,g=0,0,0,0
    pagenum = 0
    def parse(self, response):
        self.pagenum+=1
        print response.url
        #修改，新增处理函数，匹配出所有店
        allUrlAndName = self.getPage(response.url)
        selector = Selector(response)
        # all_list=selector.xpath('//div[@class="stitle util-ellipsis"]')
        # print len(all_list)
        for everyShop in allUrlAndName[0:]:
            pre_item=AlbbItem()
            urlShop=everyShop[0]
            #Url0= ip.xpath('a[2]/@href')[0].extract()
            newUrl = urlShop[0:urlShop.index('alibaba.com/')+12]+'productlist.html'
            pre_item['url'] = newUrl
            #pre_item['name'] = ip.xpath('a[2]/text()')[0].extract()
            pre_item['name'] = everyShop[1]
            if pre_item['url'] not in self.urlset:
                print u'新的新的啊'
                yield scrapy.Request(url=pre_item['url'],meta={'item':pre_item},callback=self.parse_content,
            dont_filter=True)
                # yield pre_item
            self.urlset.add(pre_item['url'])
            # yield pre_item
        # nextLink = selector.xpath('//a[@class="next"]/@href').extract()
        #修改，之前的寻找下一页没有连接，采用index找？来构造url
        index = response.url.index("?")
        nextUrl = response.url[:index]+"/"
        
        for num in range(2,271):
            nextLink=nextUrl+str(num)
            yield Request(url=nextLink,callback=self.parse,dont_filter=True)
    def parse_content(self, response):
        self.i+=1
        pre_item = response.meta['item']
        selector = Selector(response)
        product_list=selector.xpath('//div[@class="product-title"]')
        for product in product_list[0:]:
            rel_url = product.xpath('a/@href')[0].extract()
            end_url = response.urljoin(rel_url)
            # print pre_item['product_url']
            # return pre_item
            # yield
            yield scrapy.Request(url=end_url,meta={'item':pre_item},callback=self.parse_deal,
            dont_filter=True)
        if '.html?isGallery=Y' not in response.url:
            allpage=selector.xpath('//label[@class="ui-label"]/text()')[0].extract()
            all_page=allpage[5:8]
            all_page1=int(all_page)+1
            baseurl=response.url
            for n in range(2,all_page1):
                print u'第'+str(n)+u'页'
                self.w+=1
                newUrl = baseurl[0:baseurl.index('alibaba.com/')+12]+'productlist-'+ str(n) +'.html?isGallery=Y'
                yield scrapy.Request(url=newUrl,meta={'item':pre_item},callback=self.parse_content1,dont_filter=True)
                # yield pre_item
    def parse_content1(self, response):

        pre_item = response.meta['item']
        selector = Selector(response)
        product_list=selector.xpath('//div[@class="product-title"]')
        for product in product_list[0:]:
            rel_url = product.xpath('a/@href')[0].extract()
            end_url = response.urljoin(rel_url)
            # print pre_item['product_url']
            # return pre_item
            # yield
            yield scrapy.Request(url=end_url,meta={'item':pre_item},callback=self.parse_deal,
            dont_filter=True)
    def parse_deal(self, response):
        self.g+=1

        pre_item = response.meta['item']
        # product_item=productItem()
        selector = Selector(response)
        pre_item['product_name']=selector.xpath('//span[@class="title-text"]/text()')[0].extract()
        allkey=selector.xpath('//a[@class="qrPRskw"]/text()').extract()
        if len(allkey)==1:
            allkey.append('no keyword')
            allkey.append('no keyword')
        elif len(allkey)==2:
            allkey.append('no keyword')
        pre_item['product_key1'] = allkey[0]
        pre_item['product_key2'] = allkey[1]
        pre_item['product_key3'] = allkey[2]
        yield pre_item
    def getPage(self,url):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        request = urllib2.Request(url, headers = headers)
        html = urllib2.urlopen(request).read()
        patternUrlAndName = re.compile('"supplierHref":"(.*?)","supplierName":"(.*?)"',re.S)
        allUrlAndName = re.findall(patternUrlAndName,html)
        return allUrlAndName
    def close(self):
        # print self.w
        print u'共抓取类页数为'+str(self.pagenum)
        print u'一共有'+str(self.i)+u'家店铺'
        print u'一共爬取了多少个商品'+str(self.g)
        s2=time.time()
        print self.g
        print (s2-self.s1)/60 +u'分钟'
