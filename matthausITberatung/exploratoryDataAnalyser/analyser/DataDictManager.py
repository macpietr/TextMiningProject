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

    def getLemmatizedDataDictForCorpusWithoutStopWords(self, dataDict, stopWords):
        dataDictForCorpusWithoutStopWords = {}
        for key in dataDict.keys():
            helperList = []
            for opinion in dataDict[key]:
                helperList = [''.join(self.wordNetLemmatizer.lemmatize((word.strip()))) for word in opinion.split(" ") if word.strip() not in stopWords]
            dataDictForCorpusWithoutStopWords[key] = ' '.join(helperList)
        return dataDictForCorpusWithoutStopWords
