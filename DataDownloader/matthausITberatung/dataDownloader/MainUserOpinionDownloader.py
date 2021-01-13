import re

from matthausITberatung.dataDownloader.AbstractDownloader import AbstractDownloader


class MainUserOpoinionDownloader(AbstractDownloader):

    def __init__(self, listOfBeautifulSoupObjects):
        super().__init__(listOfBeautifulSoupObjects)

    def getDataBasedOnHTMLtype(self, beautifulSoupObject):
        return beautifulSoupObject.findAll('div', id=re.compile("anchor"))

    def getProcessedRow(self, userPost):
        return userPost[len(userPost) - 1].replace("|", "").lstrip().rstrip()

    def getExtractedRow(self, item):
        return item.find('div').find('div').findAll(text=True)
