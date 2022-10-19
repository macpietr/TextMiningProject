import re
import string

from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.FileWriter import FileWriter
from matthausITberatung.objectsManager.PathsManager import PathsManager


class DataCleaner:

    def cleanAndWriteData(self, nameOfDataChildDir):
        for airline in PathsManager().LIST_OF_AIRLINES:
            downloadedData = FileReader().readFile(PathsManager().DOWNLOADED_FILES_DIR, nameOfDataChildDir, airline)
            cleanedData = self.cleanData(downloadedData)
            cleanedData = self.cleanDataExtended(cleanedData)
            FileWriter(PathsManager().CLEANED_DATA_FILES_DIR, nameOfDataChildDir, airline).putDataIntoFile(cleanedData)

    def cleanDataExtended(self, data):
        data = data.lower()
        data = re.sub('[%s]' % re.escape(string.punctuation), '', data) #remove interpunction
        data = re.sub('[''""...]', '', data)
        data = re.sub('\w*\d\w*', '', data) #remove numbers
        data = re.sub('\n', '', data)
        return data

    def cleanData(self, data):
        return data\
            .replace('\\n','')\
            .replace('´','')\
            .replace('\\r','')\
            .replace('\\xa0','')\
            .replace('\\','')\
            .replace('[','')\
            .replace(']','')\
            .replace('"','')\
            .replace('\'','')\
            .replace('ttttttttttttt','')\
            .rstrip()\
            .lstrip()

    def cleanDataForNumberAnalysis(self, downloadedDataDict):
        clearedDownloadedData = {}
        for key in downloadedDataDict.keys():
            clearedDownloadedData[key] = downloadedDataDict[key]\
                .replace(' ', '').lower().replace('none\n', '').replace('n/a\n', '').replace('\n', ' ')
        return clearedDownloadedData
