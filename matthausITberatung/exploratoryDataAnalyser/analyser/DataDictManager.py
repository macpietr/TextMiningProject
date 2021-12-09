import nltk
from nltk import WordNetLemmatizer

from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.PathsManager import PathsManager


class DataDictManager:

    def __init__(self):
        nltk.download('wordnet')
        self.wordNetLemmatizer = WordNetLemmatizer()

    def getDataDictForCorpus(self, dataDict):
        return {key: [dataDict[key]] for (key, value) in dataDict.items()}

    def getDataDictFromFiles(self, partOfScrappedData):
        cleanedDataDict = {}
        for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES):
            cleanedDataDict[airline] = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR, partOfScrappedData, airline)
        return cleanedDataDict

    def getLemmatizedDataDictForCorpus(self, dataDict):
        lemmatizedDataDict = {}
        for key in dataDict.keys():
            for opinion in dataDict[key]:
                helperList = [self.wordNetLemmatizer.lemmatize(word.strip(),'v') for word in opinion.split(" ")]
                helperList = [self.wordNetLemmatizer.lemmatize(word.strip(),'n') for word in helperList]
                helperList = [self.wordNetLemmatizer.lemmatize(word.strip(),'a') for word in helperList]
                helperList = [self.wordNetLemmatizer.lemmatize(word.strip(),'r') for word in helperList]
            lemmatizedDataDict[key] = ' '.join(helperList)
        return lemmatizedDataDict

    def getDataDictWithoutStopWords(self, dataDict, stopWords):
        dataDictWithoutStopWords = {}
        for key in dataDict.keys():
            helperlist = [word.strip() for word in dataDict[key].split(" ") if word.strip() not in stopWords]
            dataDictWithoutStopWords[key] = ' '.join(helperlist)
        return dataDictWithoutStopWords
