



# This is a financial news scraper. Finds latest earnings news for a list of public companies.

# Libraries needed
import pandas
import re
import requests
from bs4 import BeautifulSoup
print ("Libraries imported")

# Variables needed
stocks=[]

# Load and read excel input file
file = pandas.read_excel('20160706 - missing earnings.xlsx')

# Results output file

#Stocks list creation
def extracting_values(file):
    values = file["stock"].dropna()
    global stocks
    stocks = values.tolist()
    print ("\nThe following stocks have been extracted and added to the stocks[] list: " + str(stocks))
soup2=0
# Creating soup objects in general
def making_soup(url):
    page = requests.get(url)
    global soup2
    soup2 = BeautifulSoup(page.content, 'html.parser')

# Searching transcriptdaily.com website
def news_search_transcriptdaily():
    for stock in stocks:
        news_found=0
        url="https://transcriptdaily.com/?s=" + str(stock)
        page = requests.get(url)
        soup1 = BeautifulSoup(page.content,'lxml')
        print ("\nSearching Transcriptdaily for the target company: " + (str(stock)))

        #Going to related news article
        for headline in soup1.find_all('a', href=re.compile(str(stock).lower())):
            exact_news = []
            exact_news.append(headline['href'])
            if news_found == 0:
                pass
            elif news_found == 1:
                break

            # Getting text from target news articles
            for news in exact_news:
                making_soup(news)
                for text in soup2.find_all('p', text=re.compile ("last issued its earnings results")):
                    print ("\nHere are the actual news lines for: " + str (stock))
                    print (text)
                    news_found = 1

                for text in soup2.find_all('p', text=re.compile ("last issued its earnings data")):
                    print ("\nHere are the actual news lines for: " + str (stock))
                    print (text)
                    news_found = 1




def news_search_dailypolitical():
    for stock in stocks:
        news_found = 0
        url = "https://www.dailypolitical.com/?s=" + str (stock)
        page = requests.get (url)
        soup1 = BeautifulSoup (page.content, 'lxml')
        print ("\nSearching Dailypolitical for the target company: " + (str (stock)))

        # Going to related news article
        for headline in soup1.find_all ('a', href=re.compile (str (stock).lower ())):
            exact_news = []
            exact_news.append (headline['href'])
            if news_found == 0:
                pass
            elif news_found == 1:
                break
                # Getting text from target news articles
            for news in exact_news:
                making_soup (news)
                for text in soup2.find_all ('p', text=re.compile ("last issued its earnings results")):
                    print ("\nHere are the actual news lines for: " + str (stock))
                    print (text)
                    news_found = 1

                for text in soup2.find_all ('p', text=re.compile ("last issued its earnings data")):
                    print ("\nHere are the actual news lines for: " + str (stock))
                    print (text)
                    news_found = 1



# Searching rttnews.com website
def news_search_rttnews():
    for stock in stocks:
        news_found=0
        url="http://www.rttnews.com/symbolsearch.aspx?symbol=" + str(stock)
        page = requests.get(url)
        soup1 = BeautifulSoup(page.content,'lxml')
        print ("\nSearching RTT News for the target company: " + (str(stock)))

# Searching marketbeat.com website
def news_search_marketbeat():
    for stock in stocks:
        news_found=0
        url="https://www.marketbeat.com/stocks/" + str(stock)
        page = requests.get(url)
        soup1 = BeautifulSoup(page.content,'lxml')
        print ("\nSearching Marketbeat for the target company: " + (str(stock)))


extracting_values(file)
news_search_transcriptdaily()




