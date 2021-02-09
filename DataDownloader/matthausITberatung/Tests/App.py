import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.airlinequality.com/airline-reviews/lufthansa/page/1/?sortby=post_date%3ADesc&pagesize=100'
beautifulSoupObject = BeautifulSoup(requests.get(url).content, "html.parser")

print(len(beautifulSoupObject))

arrayOfTables = beautifulSoupObject.findAll('table', class_='review-ratings')
print(len(arrayOfTables))

dataArray =[]

for table in arrayOfTables:
    print(str(table))
    if ('type_of_traveller' in str(table)):
        item = table.findAll('tr')
        if ('type_of_traveller' in str(item)):
            for tr in item:
                if ('type_of_traveller' in str(tr)):
                    td = tr.findAll('td')
                    dataArray.append(td[1].find(text=True))
    else:
        dataArray.append('nie ma')

print(dataArray)

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
# wyraz = '\\nhehe\\nhehe\\xa0hehe\\r\\hehe\\'
# print(wyraz)
#
# print(wyraz.replace('\\n','').replace('\\r','').replace('\\xa0','').replace('\\',''))
