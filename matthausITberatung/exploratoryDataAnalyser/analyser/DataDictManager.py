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

    def getDataDictWithoutStopWords(self, dataDict, stopWords):
        dataDictWithoutStopWords = {}
        for key in dataDict.keys():
            helperlist = []
            for line in dataDict[key]:
                helperlist.append(DataCleaner().lineWithoutStopWords(line, stopWords))
            dataDictWithoutStopWords[key] = helperlist
        return dataDictWithoutStopWords

    def createDataDictOfListsOfWords(self, dataDictOfWords):
        dataDictOfListsOfWords = {}
        for key in dataDictOfWords.keys():
            dataDictOfListsOfWords[key] = dataDictOfWords[key].split(' ')
        return dataDictOfListsOfWords

    def createDataDictOfDictsOfCountedWordsWithoutDefaultStopWords(self, dataDictOfLists, stopWords):
        dataDictOfDictsOfCountedWordsWithoutDefaultStopWords = {}
        for key in dataDictOfLists.keys():
            listOfWords = str(dataDictOfLists[key]).split(' ')
            dataDictOfDictsOfCountedWordsWithoutDefaultStopWords[key] = Counter(listOfWords)
            for word in stopWords:
                del dataDictOfDictsOfCountedWordsWithoutDefaultStopWords[key][word]
            del dataDictOfDictsOfCountedWordsWithoutDefaultStopWords[key]['']
        return dataDictOfDictsOfCountedWordsWithoutDefaultStopWords
