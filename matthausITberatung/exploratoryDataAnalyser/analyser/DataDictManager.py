from collections import Counter

import nltk
from nltk import WordNetLemmatizer

from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.PathsManager import PathsManager


class DataDictManager:

    def __init__(self):
        self.wordNetLemmatizer = WordNetLemmatizer()

    def getDataDictForCorpus(self, dataDict):
        return {key: [dataDict[key]] for (key, value) in dataDict.items()}

    def getDataDictFromFiles(self, parentDir, partOfScrappedData):
        cleanedDataDict = {}
        for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES):
            cleanedDataDict[airline] = FileReader().readFile(parentDir, partOfScrappedData,
                                                             airline)
        return cleanedDataDict

    def getLemmatizedDataDictForCorpus(self, dataDict):
        nltk.download('wordnet')
        lemmatizedDataDict = {}
        for key in dataDict.keys():
            for opinion in dataDict[key]:
                helperList = [self.wordNetLemmatizer.lemmatize(word.strip(), 'v') for word in opinion.split(" ")]
                helperList = [self.wordNetLemmatizer.lemmatize(word.strip(), 'n') for word in helperList]
                helperList = [self.wordNetLemmatizer.lemmatize(word.strip(), 'a') for word in helperList]
                helperList = [self.wordNetLemmatizer.lemmatize(word.strip(), 'r') for word in helperList]
            lemmatizedDataDict[key] = ' '.join(helperList)
        return lemmatizedDataDict

    def getDataDictWithoutStopWords(self, dataDict, stopWords):
        dataDictWithoutStopWords = {}
        for key in dataDict.keys():
            helperlist = [word.strip() for word in dataDict[key].split(" ") if word.strip() not in stopWords]
            dataDictWithoutStopWords[key] = ' '.join(helperlist)
        return dataDictWithoutStopWords

    def createDataDictOfListsOfWords(self, dataDictOfWords):
        dataDictOfListsOfWords = {}
        for key in dataDictOfWords.keys():
            dataDictOfListsOfWords[key] = dataDictOfWords[key].split(' ')
        return dataDictOfListsOfWords

    def createDataDictOfDictsOfCountedWordsWithoutDefaultStopWords(self, dataDictOfListsOfWords, stopWords):
        dataDictOfDictsOfCountedWordsWithoutDefaultStopWords = {}
        for key in dataDictOfListsOfWords.keys():
            dataDictOfDictsOfCountedWordsWithoutDefaultStopWords[key] = Counter(dataDictOfListsOfWords[key])
            for word in stopWords:
                del dataDictOfDictsOfCountedWordsWithoutDefaultStopWords[key][word]
            del dataDictOfDictsOfCountedWordsWithoutDefaultStopWords[key]['']
        return dataDictOfDictsOfCountedWordsWithoutDefaultStopWords
