# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:15:11 2017
@author: simeon
WEB SCRAPER for stocks info. Tradespoon real world project. 
"""
#Modules needed
import re
import urllib2
import pandas
from bs4 import BeautifulSoup
print "Libraries imported"
#Lists needed
values=[]
stocks=[]


#Load and read excel file
file = pandas.read_excel('20160706 - missing earnings - Copy.xlsx')

#Stocks list creation
def extracting_values(file):
    values=file["stock"].values
    stocks= values.tolist()
    del stocks[-4:]
    print "\nThe following stocks have been extracted and added to the stocks[] list: " + str(stocks)

#Going to news website for each stock.
for stock in stocks:
    news_found=0
    news_website="https://transcriptdaily.com/?s=" + str(stock)
    hdr = {'Accept': 'text/html,application/xhtml+xml,*/*',"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
    req=urllib2.Request(news_website,headers=hdr)
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html)
    print"\nLooking for news related to the target company: " + (str(stock))
#Getting all news links    
    for link in soup.find_all('a', href=re.compile(str(stock).lower())):
        exact_news=[]
        exact_news.append(link['href'])
        if news_found==0:
            pass
        elif news_found==1:
            break
#Getting text from target news articles        
        for news in exact_news:
            news_text=0
            news_text=news
            req_news=urllib2.Request(news_text,headers=hdr)
            html_news = urllib2.urlopen(req_news).read()
            target_news_soup=BeautifulSoup(html_news)
            for text in target_news_soup.find_all('p', text=re.compile("last issued its earnings results")):
                print "\nHere are the actual news lines for: " + str(stock)
                print text
                news_found=1
            for text in target_news_soup.find_all('p', text=re.compile("last issued its earnings data")):
                print "\nHere are the actual news lines for: " + str(stock)
                print text
                news_found=1
print "\nAll done!"

    
    

 
    
    


