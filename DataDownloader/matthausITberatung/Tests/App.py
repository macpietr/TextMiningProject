import requests
from bs4 import BeautifulSoup

from matthausITberatung.Tests.DataGetter import DataGetter


url = 'https://www.airlinequality.com/airline-reviews/lufthansa/page/1/?sortby=post_date%3ADesc&pagesize=100%22'
beautifulSoupObject = BeautifulSoup(requests.get(url).content, "html.parser")
print(beautifulSoupObject.find('div', id="anchor726666").find('h2').find_all(text=True))