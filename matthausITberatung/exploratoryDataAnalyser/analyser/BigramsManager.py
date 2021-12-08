from nltk import ngrams
from matthausITberatung.objectsManager.PathsManager import PathsManager

class BigramsManager:

    def getDictOfListsOfBigrams(self, dataDict):
        dataDictParsedFromDictOfBigrams = {}
        for key in dataDict.keys():
            listOfBigrams = [' '.join(bigram) for bigram in ngrams(dataDict[key].split(), 2)]
            dataDictParsedFromDictOfBigrams[key] = listOfBigrams
        return dataDictParsedFromDictOfBigrams


    # def __getDictOfBigrams(self, dataDict):
    #     dictOfBigrams = {}
    #     for key in dataDict.keys():
    #         dictOfBigrams[key] = ngrams(dataDict[key].split(), 2)
    #     return dictOfBigrams



