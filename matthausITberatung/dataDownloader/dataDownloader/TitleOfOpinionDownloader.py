from matthausITberatung.dataDownloader.dataDownloader.AbstractDownloader import AbstractDownloader


class TitleOfOpinionDownloader(AbstractDownloader):

    def __init__(self, listOfBeautifulSoupObjects):
        super().__init__(listOfBeautifulSoupObjects)

    def getDataBasedOnHTMLtype(self, beautifulSoupObject):
        return beautifulSoupObject.findAll('h2', class_='text_header')

    def getExtractedRow(self, item):
        return item.findAll(text=True)

    def getProcessedRow(self, extractedRow):
        return str(extractedRow)