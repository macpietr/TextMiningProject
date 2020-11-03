import requests

from bs4 import BeautifulSoup

class BeautifulSoupDownloader:

    def putExtractedDataIntoFile(self, fileName, listOfHTMLtags, listOfAirLineURLs):
        with open(str(fileName) + '.txt', 'w', encoding='utf-8') as outfile:
            for url in listOfAirLineURLs:
                text = self.extractData(url, listOfHTMLtags)
                for item in text:
                    print(item, file=outfile)

    def extractData(self, url, listOfHTMLtags):
        return [' '.join(s.findAll(text=True)) for s in self.getURLcontent(url).find_all(listOfHTMLtags)]

    def getURLcontent(self, url):
        return BeautifulSoup(requests.get(url).content, "html.parser")