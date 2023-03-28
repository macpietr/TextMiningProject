import re
import string

from nltk import WordNetLemmatizer

from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.FileWriter import FileWriter
from matthausITberatung.objectsManager.PathsManager import PathsManager


class DataCleaner:

    def __init__(self):
        self.wordNetLemmatizer = WordNetLemmatizer()

    def cleanAndWriteData(self, nameOfDataChildDir):
        for airline in PathsManager().LIST_OF_AIRLINES:
            downloadedData = FileReader().readFile(PathsManager().DOWNLOADED_FILES_DIR, nameOfDataChildDir, airline)
            cleanedData = self.cleanData(downloadedData)
            if nameOfDataChildDir != 'MainMarkInOpinion':
                cleanedData = self.cleanDataExtended(cleanedData)
            FileWriter(PathsManager().CLEANED_DATA_FILES_DIR, nameOfDataChildDir, airline).putDataIntoFile(cleanedData)

    def cleanDataExtended(self, data):
        data = data.lower()
        data = re.sub('[%s]' % re.escape(string.punctuation), '', data) #remove interpunction
        data = re.sub('[''""...]', '', data)
        data = re.sub('\w*\d\w*', '', data) #remove numbers
        return data

    def cleanData(self, data):
        return data\
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

    def lineWithoutStopWords(self, line, stopWords):
        helperList = [word.strip() for word in line.split(" ") if word.strip() not in stopWords]
        return ' '.join(helperList)

    def lemmatizeLine(self, line):
        helperList = [self.wordNetLemmatizer.lemmatize(word.strip(), 'v') for word in line.split(" ")]
        helperList = [self.wordNetLemmatizer.lemmatize(word.strip(), 'n') for word in helperList]
        helperList = [self.wordNetLemmatizer.lemmatize(word.strip(), 'a') for word in helperList]
        helperList = [self.wordNetLemmatizer.lemmatize(word.strip(), 'r') for word in helperList]
        return ' '.join(helperList)