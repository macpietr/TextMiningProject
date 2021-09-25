from matthausITberatung.dataDownloader.cleaner.DataCleaner import DataCleaner
from matthausITberatung.dataDownloader.dataDownloader.AbstractDownloader import AbstractDownloader


class MainUserOpoinionDownloader(AbstractDownloader):

    def __init__(self, listOfBeautifulSoupObjects):
        super().__init__(listOfBeautifulSoupObjects)

    def getDataBasedOnHTMLtype(self, beautifulSoupObject):
        return beautifulSoupObject.findAll('div', class_='text_content')

    def getExtractedRow(self, item):
        return item.findAll(text=True)

    def getProcessedRow(self, userPost):
        userPostAsString = str(userPost)
        processedUserPost = userPostAsString[self.beginFromCharacterIfExists(userPostAsString):]
        return DataCleaner(processedUserPost).cleanData()

    def beginFromCharacterIfExists(self, userPostAsString):
        try:
            return userPostAsString.index('|') + 1
        except:
            return 1

