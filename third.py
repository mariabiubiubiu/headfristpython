# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
f=open('a.txt','w')
i=30
while True:
    url='http://maoyan.com/films?offset='  
    i=i+30
    url=(url+'%d'%i)
    my_data=requests.get(url)
    soup=BeautifulSoup(my_data.text,'lxml')
    src=soup.select('div.movie-item > a')
    for sc in src:
        f.write('%s\n'%sc.get('href'))



url111=['http://maoyan.com/films?offset=[]'.format(str(i)) for i in range(30,1200,30)]

f.close()        





'''
#app > div > div.movies-panel > div.movies-list > dl > dd:nth-child(1) > div.movie-item > a
#app > div > div.movies-panel > div.movies-list > dl > dd:nth-child(2) > div.movie-item > a
#app > div > div.movies-panel > div.movies-list > dl > dd:nth-child(3) > div.movie-item > a
'''