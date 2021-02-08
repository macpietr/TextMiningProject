from matthausITberatung.cleaner.DataCleaner import DataCleaner
from matthausITberatung.dataDownloader.AbstractDownloader import AbstractDownloader


class ReviewRatingDownloader(AbstractDownloader):

    def __init__(self, listOfBeautifulSoupObjects, reviewRatingHeader):
        super().__init__(listOfBeautifulSoupObjects)
        self.reviewRatingHeader = reviewRatingHeader

    def getDataBasedOnHTMLtype(self, beautifulSoupObject):
        return beautifulSoupObject.findAll('tr')

    def getExtractedRow(self, item):
        td = item.findAll('td')
        if (self.reviewRatingHeader in str(td)):
            return td[1].findAll(text=True)
            # TODO naprawić to (ma być zgodnie z testem App.py)


    def getProcessedRow(self, userMainMark):
        userMainMarkAsString = str(userMainMark)
        return DataCleaner(userMainMarkAsString).cleanData()
