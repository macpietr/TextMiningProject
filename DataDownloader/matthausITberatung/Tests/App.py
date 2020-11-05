import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.airlinequality.com/airline-reviews/lufthansa/page/1/?sortby=post_date%3ADesc&pagesize=100'
beautifulSoupObject = BeautifulSoup(requests.get(url).content, "html.parser")
tag = beautifulSoupObject.find('div', id=re.compile("anchor")).find('div').find('div').find_all(text=True)[2]
tag2 = tag.replace("|  ","")
print(tag2)