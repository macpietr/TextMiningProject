import requests
from bs4 import BeautifulSoup
import re

# url = 'https://www.airlinequality.com/airline-reviews/lufthansa/page/1/?sortby=post_date%3ADesc&pagesize=100'
# beautifulSoupObject = BeautifulSoup(requests.get(url).content, "html.parser")
#
# tag = beautifulSoupObject.findAll('span', itemprop='ratingValue')
#
# def tryToDecompose(tag):
#     try:
#         tag.find('em').decompose()
#         tag.find('a').decompose()
#         tag.find('strong').decompose()
#     except:
#         pass
#
# def isIndex(tstr):
#     try:
#         character = tstr.index('|')
#         return character + 1
#     except:
#         return 1
#
# dataArray=[]
# for t in tag:
#     dataArray.append(str(t.findAll(text=True)).replace("['","").replace("']","").replace("\\n","").replace("\\t","").lstrip().rstrip())
#
#
# for i in dataArray:
#     print(i)
wyraz = '\\nhehe\\nhehe\\xa0hehe\\r\\hehe\\'
print(wyraz)

print(wyraz.replace('\\n','').replace('\\r','').replace('\\xa0','').replace('\\',''))