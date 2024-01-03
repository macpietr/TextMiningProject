from collections import Counter

import nltk

from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.PathsManager import PathsManager


class DataDictManager:

    def getDataDictFromFiles(self, parentDir, partOfScrappedData):
        dataDict = {}
        for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES):
            dataDict[airline] = FileReader().readFile(parentDir, partOfScrappedData,
                                                             airline)
        return dataDict

    def getLemmatizedDataDictOfLists(self, dataDict):
        nltk.download('wordnet')
        lemmatizedDataDict = {}
        for key in dataDict.keys():
            helperList = []
            for opinion in dataDict[key]:
                helperList.append(DataCleaner().lemmatizeLine(opinion))
            lemmatizedDataDict[key] = helperList
        return lemmatizedDataDict
