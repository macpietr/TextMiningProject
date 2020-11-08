import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.airlinequality.com/airline-reviews/lufthansa/page/1/?sortby=post_date%3ADesc&pagesize=100'
beautifulSoupObject = BeautifulSoup(requests.get(url).content, "html.parser")
tag = beautifulSoupObject.findAll('div', id=re.compile("anchor"))
for t in tag:
    userPost = t.find('div').find('div').find_all(text=True)
    userPostLength = len(userPost)
    print(userPost[userPostLength-1].replace("|","").lstrip().rstrip())
    # if userPost[0]=='Not Verified':
    #     print(userPost[1])
    # else:
    #     print(userPost[2])

    # .find('div').find('div')
        # .find_all(text=True)[2]
# tag2 = tag.replace("| ","")