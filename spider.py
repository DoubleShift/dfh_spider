# -*- coding:utf-8 -*-
 
import urllib2
import re


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
        product['name'] =re.findall('<h1>(.*?)</h1>',page,re.S)
        product['picture'] =re.findall('rel="zoom-id:Zoomer2" rev="(.*?)" title="',page,re.S)
        product['stock'] =re.findall(u'库存: <span>(.*?)</span>',page,re.S)
        product['date'] =re.findall(u'有效日期:<span>(.*?)</span>',page,re.S)
        product['score'] = re.findall(u'你将获得 <span id=\'j2t-pts\'>(.*?)</span> 积分',page,re.S)
        #排除匹配的第一个购物车价格
        product['price'] = re.findall('<span class="price">(.*?)</span>',page,re.S)[1]
        return product

    #获取页面的内容
    def getPage(self,url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    def save(self,content):
        # f = open("log.txt","w+")
        # f.write(str(content))
        print content


 
# 36个一页，“产品1到36，共计359件” 通过这一项来计算多少页
spider = Spider('http://www.dfh.fi/simplified/updates.html?limit=36&p=')

#抓取商品网址列表
endpage = spider.getTotalPages()
contents = []
for i in range(1,endpage):
    contents += spider.getPageList(i)

print len(contents)

for i in contents:
    content = spider.getDetail(i)
    spider.save(content)

spider.save(spider.getDetail('http://www.dfh.fi/simplified/updates/1050.html'))
