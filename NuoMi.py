# -*- coding=utf-8 -*-
import re
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
cities=['nj']
def downloadPage():
    for city in cities:
        url='http://%s.nuomi.com'%city
        page=urllib2.urlopen(url).read()
        return page
def parserPage(page):
    item_title=[]
    item_pop_n=[]
    item_c_price=[]
    item_rates=[]
##    item_o_price=[]
    soup=BeautifulSoup(page)
    title=soup.findAll('h3')
    for i in range(4,len(title)-4):
        item_title.append(''.join(title[i].contents[1].string.strip().split()))##获取物品标题
        
    people= soup.findAll("div",{"class":"totalpop"})
    for i in range(len(people)):
        item_pop=people[i].string
        item_pop_n.append(item_pop[0:len(item_pop)-1])          ##获取购买人数
    price=soup.findAll("span",{"class":"prices"})
    for i in range(1,len(price),2):
        item_price=price[i].string
        item_c_price.append(item_price[:])                  ##获取当前的价格
    discount=soup.findAll('span',style="line-height:50px;")
    for i in range(len(discount)):
        item_discount=discount[i].string.strip()
        item_rates.append(item_discount[0:len(item_discount)-1])
##        item_o_price.append(item_c_price/discount_r)          
    return item_title,item_pop_n,item_c_price,item_rates
if __name__=="__main__":
    file=open(r'd:\textdada.csv','w')
    page=downloadPage()
    title,people,curprice,rate=parserPage(page)
    for x,y,z,k in zip(title,people,curprice,rate):
        file.write(x.encode('utf-8')+','+y.encode('utf-8')+','+z.encode('utf-8')+','+k.encode('utf-8')+'\n')
        
        
    file.close()
    
    print u"输入成功"
    
    





































































































































































        
        
    
