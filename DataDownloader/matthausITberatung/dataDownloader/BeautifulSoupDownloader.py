import requests

from bs4 import BeautifulSoup

class BeautifulSoupDownloader:

    def getListOfBeautifulSoupObject(self, listOfUrls):
        listOfBeautifulSoupObjects = []
        for url in listOfUrls:
            listOfBeautifulSoupObjects.append(self.getBeautifulSoupObject(url))
        return listOfBeautifulSoupObjects

    def getBeautifulSoupObject(self, url):
        return BeautifulSoup(requests.get(url).content, "html.parser")
