from matthausITberatung.dataDownloader.dataDownloader.AbstractDownloader import AbstractDownloader

class ReviewRatingDownloader(AbstractDownloader):

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
                        return td[1].find(text=True)
        else:
            return None

    def getProcessedRow(self, userMainMark):
        return str(userMainMark)
