# -*- coding:utf-8 -*-

import urllib2
import time
import re
import datetime
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from log import logger


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)




class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    url = db.Column(db.String(256),index=True,unique=True)
    picture = db.Column(db.String(256))
    stock = db.Column(db.String(4))
    date = db.Column(db.String(16))
    score = db.Column(db.Integer)

    def __init__(self,name,url,picture,stock,date,score):
        self.name = name
        self.url = url
        self.picture = picture
        self.stock = stock
        self.date = date
        self.score = score


class Prices(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)




#抓取
class Spider:
 
    #页面初始化
    def __init__(self,starturl):
        self.siteURL = starturl

    #取分页中得商品网址
    def getPageList(self,index):
        url = self.siteURL + str(index)
        page = self.getPage(url)
        pagelists = re.findall('<h2 class="product-name"><a href="(.*?)" title="',page,re.S)
        return pagelists

    #取分页总数
    def getTotalPages(self):
        url = self.siteURL + str(1)
        page = self.getPage(url)
        #utf-8 编码的中文，需要+
        totalPages = re.findall(u"共计<span>(.*?)</span>件",page,re.M)
        #359项，36个一页，一共是 359/36 +1 页
        total = int(totalPages[0])/36 + 1
        return total

    #获取商品详细信息
    def getDetail(self,url):
        page = self.getPage(url)
        product = {}
        product['name']     =   re.findall('<h1>(.*?)</h1>',page,re.S)[0]
        product['url']      =   url
        product['picture']  =   re.findall('rel="zoom-id:Zoomer2" rev="(.*?)" title="',page,re.S)[0]
        product['stock']    =   re.findall(u'库存: <span>(.*?)</span>',page,re.S)[0]
        product['date']     =   re.findall(u'有效日期:<span>(.*?)</span>',page,re.S)[0]
        product['score']    =   int(re.findall(u'你将获得 <span id=\'j2t-pts\'>(.*?)</span> 积分',page,re.S)[0])

        #排除匹配的第一个购物车价格
        product['price'] = re.findall('<span class="price">(.*?)</span>',page,re.S)[1]
        #排除欧元符号
        product['price'] = product['price'].replace(u"€ ",u"")
        return product

    #获取页面的内容
    def getPage(self,url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    def save(self,product):

            content = Products(
                product['name'],
                product['url'],
                product['picture'],
                product['stock'],
                product['date'],
                product['score'])
            db.session.add(content)
            db.session.commit()
            logger.DebugMessage('insert :'+ product['url'])
            return True




# 36个一页，“产品1到36，共计359件” 通过这一项来计算多少页
# spider = Spider('http://www.dfh.fi/simplified/updates.html?limit=36&p=')
# content = spider.getDetail('http://www.dfh.fi/simplified/updates/1050.html')
# print content
# spider.save(content)
#
# #抓取商品网址列表
# endpage = spider.getTotalPages()
# contents = []
# for i in range(1,2):
#     contents += spider.getPageList(i)
#
# logger.DebugMessage('Total Pages:'+ str(len(contents)))
#
#
# for i in contents:
#     content = spider.getDetail(i)
#     spider.save(content)


@app.route("/")
def hello():
    spider = Spider('http://www.dfh.fi/simplified/updates.html?limit=36&p=')
    content = spider.getDetail('http://www.dfh.fi/simplified/updates/1050.html')
    spider.save(content)

    endpage = spider.getTotalPages()
    contents = []
    for i in range(1,2):
        contents += spider.getPageList(i)
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)

