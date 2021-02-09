from matthausITberatung.cleaner.DataCleaner import DataCleaner
from matthausITberatung.dataDownloader.AbstractDownloader import AbstractDownloader


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


        #TODO make better condition whcich will return NONE only if there won't be particular reviewRatingHeader insted of checking it for every <td>



    def getProcessedRow(self, userMainMark):
        userMainMarkAsString = str(userMainMark)
        return DataCleaner(userMainMarkAsString).cleanData()
