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
        #TODO make better condition whcich will return NONE only if there won't be particular reviewRatingHeader insted of checking it for every <td>
        if (self.reviewRatingHeader in str(td)):
            return td[1].findAll(text=True)



    def getProcessedRow(self, userMainMark):
        userMainMarkAsString = str(userMainMark)
        return DataCleaner(userMainMarkAsString).cleanData()
