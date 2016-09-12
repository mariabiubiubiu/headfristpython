# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:43:58 2014
@author: Administrator
"""
import re
import urllib.request
import time
import json
import sys
import string

sys.getdefaultencoding()


class Movie:
    def __init__(self,JsonInfo):
        #print(JsonInfo)

        if 'title' in JsonInfo:
            self.Name = ''.join(JsonInfo['title'])
            #self.Name = json.dumps(JsonInfo['title'])
            #self.Name = "你好"
            #self.Name = JsonInfo['title']
            #print(JsonInfo['title'])
            #print(self.Name)
        if 'attrs' in JsonInfo and 'alt_title' in JsonInfo['attrs']:
            self.Aka = JsonInfo['attrs']['alt_title'];
            #print(JsonInfo['attrs']['alt_title'])
        if  self.Aka is None and 'alt_title' in JsonInfo:
            self.Aka = JsonInfo['alt_title']
            #print(JsonInfo['alt_title'])
        if 'rating'in JsonInfo and 'average' in JsonInfo['rating']:
            self.Rate = JsonInfo['rating']['average']
        if 'rating'in JsonInfo and 'numRaters'in JsonInfo['rating']:
            self.RateNum = JsonInfo['rating']['numRaters']
        if 'attrs' in JsonInfo and 'director' in JsonInfo['attrs']:
            self.Directors = "".join(JsonInfo['attrs']['director'])
        if 'attrs' in  JsonInfo and  'cast' in JsonInfo['attrs']:
            #self.Casts = json.dumps(JsonInfo['attrs']['cast'])
            #self.Casts = "".join(JsonInfo['attrs']['cast'])
            #self.Casts = JsonInfo['attrs']['cast']

           for x in JsonInfo['attrs']['cast']:
                if not self.Casts:
                    self.Casts = x
                else:
                   self.Casts += ", "+x


        if 'attrs' in JsonInfo and  'pubdate' in JsonInfo['attrs']:
            self.Year = "".join(JsonInfo['attrs']['pubdate'])
        if 'attrs' in JsonInfo and 'language' in JsonInfo['attrs']:
            self.Language = "".join((JsonInfo['attrs']['language']))

        if 'id' in JsonInfo:
            pattern = re.compile(r'\d+')
            self.Id = "".join(GetRE(JsonInfo['id'],pattern))
        if 'attrs' in JsonInfo and 'movie_duration' in JsonInfo['attrs']:
            self.Duration = "".join(JsonInfo['attrs']['movie_duration'])
        if 'attrs'in JsonInfo and 'movie_type' in JsonInfo['attrs']:
            self.Genres = "".join(JsonInfo['attrs']['movie_type'])
        if 'attrs' in JsonInfo and 'country' in JsonInfo['attrs']:
            self.Country = "".join(JsonInfo['attrs']['country'])
        if 'comments_count' in JsonInfo:
            self.Comments = JsonInfo['comments_count']
        if 'reviews_count' in JsonInfo:
            self.Reviews = JsonInfo['reviews_count']
        
    Name = None
    NameOriginal = None
    Aka = None
    Rate = None
    RateNum = 0
    Directors = None
    Language = None
    Casts = None
    Year = None
    Duration = None;
    Genres = None
    Id = None
    Country = None
    Comments = None
    Reviews = None

def GetRE(content,regexp):
    result = re.findall(regexp, content)
    return result

def GetContent(url):
    #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'}
    #headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    #req = urllib.request.Request(url = url,headers = headers);
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    req = urllib.request.Request(url= url)
    while True:
        flag = 1;
        try:
            content = urllib.request.urlopen(req).read()
            s2 = str(content, encoding='utf-8')
            time.sleep(3)
        except:
            print(sys.exc_info()[0],":", sys.exc_info()[1])
            flag = 1
            s2 = ''
            time.sleep(3)
        if flag == 1:
            break;

    #return s2
    return s2


def GetAllTagList():
    """
    http://book.douban.com/tag/
    获取全部分类列表
    """
    content = GetContent("http://movie.douban.com/tag/")
    regexp = r"<td><a href=\"/tag/(.+)\">\1";
    #print(GetRE(content,regexp))
    return GetRE(content,regexp);

def GetMovieWithTag(tag):
    """
    http://book.douban.com/tag/:tag?start=0&type=T
    获取书本信息
    """
    startid = 0;
    TotalList = [];
    while True:
        url = "http://movie.douban.com/tag/"+tag+"?start="+str(startid)+"&type=T"
        #print(url)
        content = GetContent(url)
        cut_idx = content.find('block5 movie_show');
        #截断右边栏的推荐书目
        if cut_idx >= 0:
            content = content[:cut_idx]
        #提取书本ID
        regexp = r'https://movie.douban.com/subject/(\d+)/'
        #去重
        MovieIdList = list(set(GetRE(content,regexp)))
        if len(MovieIdList) != 0:
            TotalList += MovieIdList
            startid += 20;
            time.sleep(2)
        else:
            break
    #print(TotalList)
    #print(list(set(TotalList)))
    return list(set(TotalList))

def getMovieInfo(id):
    """
    根据API来获取书本信息
    """
    url = 'http://api.douban.com/v2/movie/'+id;
    print(url)
    content = GetContent(url)
    JsonInfo = json.loads(content)
    #JsonInfo = json.dumps(content)
    #print(JsonInfo)
    movie = Movie(JsonInfo);
    return movie
"""
def WriteItem(fh,book):
    fh.write('%s\n'%book.Name);
    fh.write('\tId:%s\n'%book.Id);
    fh.write('\tRate:%s\n'%book.Rate.encode('gbk','ignore'));
    fh.write('\tRate Number:%d\n'%book.RateNum);
    fh.write('\tPrice:%s\n'%book.Price.encode('gbk','ignore'));
    fh.write('\tPublish Date:%s\n'%book.Pubdate.encode('gbk','ignore'));
    fh.write('\tPublisher:%s\n\n'%book.Publisher.encode('gbk','ignore'));
"""


def WriteItem(fh,movie):
    if movie.Name:

        try:
            fh.write('%s\n'%movie.Name);
            """
            print(movie.Name)
            #print('\u7537'.decode('unicode_escape'))
            s = '\u305f'
            s = movie.Name
            print(type(movie.Name))
            s= "\u30a6\u30eb\u30c8\u30e9\u30bb\u30d6\u30f3 \u6a21\u9020\u3055\u308c\u305f\u7537"
            s = movie.Name
            print(type(s))
            print(s)
            print(json.loads('"%s"' % s))
        """
        except:
            l = movie.Aka.find('/')
            if l > 0:
                fh.write('%s\n'%movie.Aka[0:l])
            else:
                fh.write('%s\n'%movie.Aka)
        #fh.write('%s\n' % movie.Name.encode('latin-1').decode('unicode_escape'));
    if movie.Id:
        fh.write('\tId:%s\n'%movie.Id)
    if movie.Aka:
        fh.write('\tAlternate Name:%s\n'%movie.Aka);
    fh.write('\tRate Number:%d\n'%movie.RateNum);
    fh.write('\tRate:%s\n'%movie.Rate);
    if movie.Directors:
        #fh.write('\tDirectors:%s\n'%movie.Directors.encode('gb18030'));
        try:
            fh.write('\tDirectors:%s\n'%movie.Directors);
        except:
            fh.write("")
    fh.write('\tLanguage:%s\n'%movie.Language);
    if movie.Casts:
        #fh.write('\tCasts:%s\n'%movie.Casts.encode('gb18030'));
        try:
            fh.write('\tCasts:%s\n'%movie.Casts);
        except:
            fh.write('\tCasts:')
            for x in movie.Casts.split(','):
            #fh.write('\t%s\n'%x)
            #print(type(x))
            #print(x)
                try:
                    fh.write('\t%s,'%x)
                except:
                #fh.write('\t%s\n'%x.encode('gbk','ignore').decode('utf-8'))
                    fh.write("");
            fh.write('\n')
    fh.write('\tYear:%s\n'%movie.Year);
    fh.write('\tDuration:%s\n'%movie.Duration);
    fh.write('\tGenres:%s\n'%movie.Genres);
    fh.write('\tCountry:%s\n\n\n'%movie.Country);
    #fh.write('\tComments:%s\n'%movie.Comments);
    #fh.write('\tReviews:%s\n\n'%movie.Reviews);

def GetAllIdOfBook():
    print("get id")
    taglist = GetAllTagList();
    taglist = ['墨西哥']
    f = open('SciFic_1.txt','w');
    for tag in taglist:
        f.write('%s\n'%(tag))
        #print(tag)
        tag = urllib.request.quote(tag)
        MovieIdList = GetMovieWithTag(tag)
        for MovieId in MovieIdList:
            f.write('\t%s\n'%(MovieId))
    f.close();

def scrawlAllBook():
    BookIdList = [];
    IDListFile = open('cult.txt','r')
    #IDListFile = open('MovieId.txt','r')
    for line in IDListFile:
        id = GetRE(line,r'^\t(\d+)$');
        if id == []:
            continue
        BookIdList.append(id[0])
    IDListFile.close()
    BookIdList = list(set(BookIdList))
    #print(BookIdList)
    file_h = open('SciFic_movie_detail_4.txt','a+')
    for movieid in BookIdList:
        MovieInfo = getMovieInfo(movieid);
        #print(MovieInfo.Id,MovieInfo.Name)
        WriteItem(file_h,MovieInfo)
        time.sleep(2)



if __name__ == "__main__":
    #爬取所有书ID保存到文件中
    #GetAllIdOfBook()
    scrawlAllBook()
    print("hello")
    #GetAllIdOfBook()

#scrawlAllBook()

#GetAllIdOfBook()


