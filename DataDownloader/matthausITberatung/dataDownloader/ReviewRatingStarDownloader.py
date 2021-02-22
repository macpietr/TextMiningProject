from matthausITberatung.cleaner.DataCleaner import DataCleaner
from matthausITberatung.dataDownloader.AbstractDownloader import AbstractDownloader


class ReviewRatingStarDownloader(AbstractDownloader):

    def __init__(self, listOfBeautifulSoupObjects, reviewRatingHeader):
        super().__init__(listOfBeautifulSoupObjects)
        self.reviewRatingHeader = reviewRatingHeader

    def getDataBasedOnHTMLtype(self, beautifulSoupObject):
        table = beautifulSoupObject.findAll('table', class_='review-ratings')
        table.remove(table[0])
        return table

    def getExtractedRow(self, table):
        if (self.reviewRatingHeader in str(table)):
            item = table.findAll('tr')
            if (self.reviewRatingHeader in str(item)):
                for tr in item:
                    if (self.reviewRatingHeader in str(tr)):
                        td = tr.findAll('td')
                        span = td[1].findAll('span')
                        counter = -1
                        for star in span:
                            if ('\"star fill\"' in str(star)):
                                counter = counter + 1
                        return span[counter].find(text=True)
        else:
            return None

    def getProcessedRow(self, userMainMark):
        userMainMarkAsString = str(userMainMark)
        return DataCleaner(userMainMarkAsString).cleanData()
