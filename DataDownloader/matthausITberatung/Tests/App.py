import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.airlinequality.com/airline-reviews/lufthansa/page/1/?sortby=post_date%3ADesc&pagesize=100'
beautifulSoupObject = BeautifulSoup(requests.get(url).content, "html.parser")
tag = beautifulSoupObject.findAll('div', class_='text_content')

t = tag[0]
t.find('em').decompose()
t.find('a').decompose()
t.find('strong').decompose()
t2 = t.findAll(text=True)
tstr = str(t2)
character = tstr.index('|')
print(tstr[character+1:].lstrip().rstrip())

# dataArray = []
# for t in tag:
#     print(t)
#     userPost = t.find('em')
#     dataArray.append(userPost)

#
# for item in dataArray:
#     print(item)
# if userPost[0]=='Not Verified':
#     print(userPost[1])
# else:
#     print(userPost[2])

# .find('div').find('div')
# .find_all(text=True)[2]
# tag2 = tag.replace("| ","")
