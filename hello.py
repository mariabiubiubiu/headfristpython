from bs4 import BeautifulSoup
import types
with open('C:/Users/maria/Desktop/hello.html','rb')as hello:
    Soup=BeautifulSoup(hello,'lxml')
    images=Soup.select('#app > div > div.movies-panel > div.movies-list > dl > dd > div.movie-item > a > div > img:nth-of-type(2)')
    types=Soup.select('#app > div > div.tags-panel > ul > li:nth-of-type(1) > ul > li > a')
    areas=Soup.select('#app > div > div.tags-panel > ul > li:nth-of-type(2) > ul > li > a')
    years=Soup.select('#app > div > div.tags-panel > ul > li:nth-of-type(3) > ul > li > a')
for year,area,type,image in zip(years,areas,types,images):
    data={
        'year':year.get_text(),
        'area':area.get_text(),
        'type':type.get_text(),
        'ima':image.get('src')
        }
    print(data)







'''    
#app > div > div.tags-panel > ul > li:nth-child(1) > ul > li > a
#app > div > div.tags-panel > ul > li:nth-child(2) > ul > li > a   
#app > div > div.tags-panel > ul > li:nth-child(3) > ul > li > a
#app > div > div.movies-panel > div.movies-list > dl > dd:nth-child(2) > div.movie-item > a > div > img:nth-child(2)
'''