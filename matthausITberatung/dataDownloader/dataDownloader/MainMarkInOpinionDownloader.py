from matthausITberatung.dataDownloader.dataDownloader.AbstractDownloader import AbstractDownloader


class MainMarkInOpinionDownloader(AbstractDownloader):

    def __init__(self, listOfBeautifulSoupObjects):
        super().__init__(listOfBeautifulSoupObjects)

    def getDataBasedOnHTMLtype(self, beautifulSoupObject):
        return beautifulSoupObject.findAll('span', itemprop='ratingValue')

    def getExtractedRow(self, item):
        return item.findAll(text=True)

    def getProcessedRow(self, userMainMark):
        return str(userMainMark)

