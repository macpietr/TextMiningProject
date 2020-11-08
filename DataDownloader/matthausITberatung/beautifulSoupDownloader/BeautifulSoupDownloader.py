import requests

from bs4 import BeautifulSoup

class BeautifulSoupDownloader:

    def getBeautifulSoupObject(self, url):
        return BeautifulSoup(requests.get(url).content, "html.parser")


    def extractData(self, url, listOfHTMLtags):
        return [' '.join(s.findAll(text=True)) for s in self.getURLcontent(url).find_all(listOfHTMLtags)]

    def getURLcontent(self, url):
        return BeautifulSoup(requests.get(url).content, "html.parser")