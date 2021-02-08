from matthausITberatung.cleaner.DataCleaner import DataCleaner
from matthausITberatung.dataDownloader.AbstractDownloader import AbstractDownloader


class AircraftDownloader(AbstractDownloader):

    def __init__(self, listOfBeautifulSoupObjects):
        super().__init__(listOfBeautifulSoupObjects)

    def getDataBasedOnHTMLtype(self, beautifulSoupObject):
        return beautifulSoupObject.findAll('table',class_='review-ratings')

    def getExtractedRow(self, item):
        trtag = item.find('tr')
        if('Aircraft' in str(trtag)):
            result = trtag.find('td',class_='review-value').findAll(text=True)
            return result

    def getProcessedRow(self, userMainMark):
        userMainMarkAsString = str(userMainMark)
        return DataCleaner(userMainMarkAsString).cleanData()
