# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


def cal_(Url):
    f=open('b.txt','w',encoding='utf-8')
    my_ying=requests.get(Url)
    ping=BeautifulSoup(my_ying.text,'lxml')
    names=ping.select('body > div.banner > div > div.celeInfo-right.clearfix > div.movie-brief-container > h3')
    judges=ping.select('div.comment-content')
    #print(judges)
    for judge in judges:
        data={
            'judge':judge.get_text()  
            } 
        print(data)
        f.write('%s'%judge.get_text())           
    
    #print(list(judges.stripped_strings)
   
    for name in names:
        data1={
            'name':name.get_text(),
            #'judge':list(judge.stripped_strings)  
            }
        print(data1)
        f.write('%s'%name.get_text())

    

def bianli():
    
    IDList=open('a.txt','r')
    MoviePage=[]
    for line in IDList:
        if id == []:
            continue
        url='http://maoyan.com'+line.strip('\n')
        cal_(url)
    IDList.close()
    MoviePage = list(set(MoviePage))    
    

bianli()






'''
#app > div > div.main-content > div > div.tab-content-container > div.tab-desc.tab-content.active > div:nth-child(4) > div.mod-content > div > ul > li:nth-child(1) > div.main > div.comment-content
'''