# -*- coding=utf-8 -*-
﻿import urllib2
import re
import time
from BeautifulSoup import BeautifulSoup
from math import ceil

def category_page_num(i):#返回每个分类下所有产品所要用到的页数
    number=re.compile('<em>(.*?)</em>',re.DOTALL).findall(categories)
    n=number[i].strip()[1:-1]
    return int(ceil(int(n)/30.0))
    
def category_name(i):
    name=re.compile('<a href\=\"\/\?\_category\=.*?\">(.*?)<em>',re.DOTALL).findall(categories)
    return name[i].decode('utf-8').encode('gb2312')
def download_urls_objects():
    urls=[]
    soup_sum=[]
    names=[]
    category=re.compile('<a href\=\"\/\?\_category\=(.*?)\">',re.DOTALL).findall(categories) #利用正则表达式找到各个分类的标号，并返回一个列表
    for i in range(len(category)):
      n=category_page_num(i)
      name=category_name(i)
      names.append(name)
      for numbers in range(1,n+1):
        urls.append(url+'/?_category=%s&page=%d'%(category[i],numbers))
    for url_t in urls:
                    page=urllib2.urlopen(url_t)
                    soup_cat=BeautifulSoup(page)
                    soup_sum.append(soup_cat)
    for w in soup_sum:
                    lemons=w
    for n in names:
                    qqq=n
    return soup_sum,names
  
        
def parser_page(soup_cat):
        titles=[]
        prices=[]
        people=[]
        title_o=soup_cat.findAll('h2')
        for n in range(len(title_o)):
                title=title_o[n].contents[0].prettify()
                titles.append(re.compile('</strong>(.*)</a>',re.DOTALL).findall(title)[0].strip())#找到标题
        price_o=soup_cat.findAll("div",{"class":"con-pre"})
        for m in range(len(price_o)):
                try:
                        price=re.compile('</span>(.*)<span class="small_price">(.*)</span>',re.DOTALL).findall(price_o[m].prettify())[0]
                except IndexError:
                        price=('0','.0')
                prices.append(price[0].strip()+price[1].strip())
        people_o=soup_cat.findAll("span",{"class":"n_buy_ed"})
        for k in range(len(people_o)):
                people.append(re.compile('<strong>(.*)</strong>',re.DOTALL).findall(people_o[k].prettify())[0].strip())
        return titles,prices,people
def summation_x(n):
    global sum_x
    sum_x=sum_x+num[n]
    b=sum_x
    return b
def summation_y(n):
    global sum_y
    sum_y=sum_y+num[n+1]
    a=sum_y
    return a
if __name__=="__main__":
    start=time.time()
    cities=['nangjing']
    global url
    global soup
    global categories
    global num
    sum_x=0
    sum_y=0
    num=[]
    for city in cities:
      url='http://%s.lashou.com'%city #get the url of citie
      index_page=urllib2.urlopen(url)    #get the indexpage object
      soup=BeautifulSoup(index_page)
      categories=soup.findAll('dd')[-2].prettify()+soup.findAll('dd')[-1].prettify()
    
    soup_sum,names=download_urls_objects()
    for m in range(len(names)):
        num.append(category_page_num(m))
    num.insert(0,0)
    
    for n in range(len(names)):
        file=open(r'd:\lashounanjing\20120326%d.csv'%n,'w')
        for i in range(summation_x(n),summation_y(n)):
            titles,prices,people=parser_page(soup_sum[i])
            for x,y,z in zip(titles,prices,people):
                    
                    file.write(x+','+y+','+z+'\n')
        file.close()
    print "elaapsed time:%s"%(time.time()-start)
