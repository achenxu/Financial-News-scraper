



# This is a financial news scraper. Finds latest earnings news for a list of public companies.

# Libraries needed
import time
import pandas
import xlsxwriter
import re
import requests
from bs4 import BeautifulSoup
print ("Libraries imported")

#Tracks how much time the script runs
start = time.time()

# Variables needed
stocks=[]
soup2=0
news_found = 0
row=1
col=0

# Load and read excel input file
file = pandas.read_excel('20160706 - missing earnings.xlsx')

# Results output file
output_file = xlsxwriter.Workbook('Results.xlsx')
worksheet = output_file.add_worksheet()

#Stocks list creation
def extracting_values(file):
    values = file["stock"].dropna()
    global stocks
    stocks = values.tolist()
    print ("\nThe following stocks have been extracted and added to the stocks[] list: " + str(stocks))


# Creating soup objects in general
def making_soup(url):
    page = requests.get(url)
    global soup2
    soup2 = BeautifulSoup(page.content, 'html.parser')

# Searching transcriptdaily.com website
def news_search_transcriptdaily():
    global news_found
    news_found =0
    url="https://transcriptdaily.com/?s=" + str(stock)
    page = requests.get(url)
    soup1 = BeautifulSoup(page.content,'lxml')
    print ("\nSearching Transcriptdaily for the target company: " + (str(stock)))

    #Going to related news article
    for headline in soup1.find_all('a', href=re.compile(str(stock).lower())):
        exact_news = []
        if str(stock) in headline.text:
            exact_news.append(headline['href'])
        else:
            pass

        if news_found == 0:
            pass
        elif news_found == 1:
            break

        # Getting text from target news articles
        for news in exact_news:
            making_soup(news)
            global col
            col = 5

            for text in soup2.find_all('p', text=re.compile ("last issued its earnings results")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break

            for text in soup2.find_all('p', text=re.compile ("last issued its earnings data")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break

            for text in soup2.find_all ('p', text=re.compile ("last announced its quarterly earnings results")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break

            for text in soup2.find_all ('p', text=re.compile ("last released its quarterly earnings results")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break

            for text in soup2.find_all ('p', text=re.compile ("last announced its earnings results")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break


# Searching dailypolitical.com website
def news_search_dailypolitical():
    global news_found
    news_found == 0
    url = "https://www.dailypolitical.com/?s=" + str (stock)
    page = requests.get (url)
    soup1 = BeautifulSoup (page.content, 'lxml')
    print ("\nSearching Dailypolitical for the target company: " + (str (stock)))

    # Going to related news article
    for headline in soup1.find_all ('a', href=re.compile (str (stock).lower ())):
        exact_news = []
        if str(stock) in headline.text:
            exact_news.append(headline['href'])
        else:
            pass

        # Getting text from target news articles
        for news in exact_news:
            making_soup (news)
            global col
            col = 5

            for text in soup2.find_all ('p', text=re.compile ("last issued its earnings results")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break

            for text in soup2.find_all ('p', text=re.compile ("last issued its earnings data")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break

            for text in soup2.find_all ('p', text=re.compile ("last announced its quarterly earnings results")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break

            for text in soup2.find_all ('p', text=re.compile ("last released its quarterly earnings results")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break

            for text in soup2.find_all ('p', text=re.compile ("last announced its earnings results")):
                print ("\nHere are the actual news lines for: " + str (stock))
                print (text)
                news_found = 1
                break

    text = 'No news found'



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

# Code start
extracting_values(file)
for stock in stocks:
    news_search_transcriptdaily()

    if news_found == 1:
        pass

    elif news_found == 0:
        news_search_dailypolitical()

    else:
        print("Problem with script")

print ('\nAll done!')
end = time.time()
print ("\nTotal time for running:")
print(end - start)



