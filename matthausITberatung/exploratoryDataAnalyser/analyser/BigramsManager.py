from nltk import ngrams
from matthausITberatung.objectsManager.PathsManager import PathsManager

class BigramsManager:

    def getDataDictParsedFromDictOfBigrams(self, mainOpinionsCorpus):
        dataDictParsedFromDictOfBigrams = {}
        for airline in PathsManager().LIST_OF_AIRLINES:
            listOfBigrams = [' '.join(bigram) for bigram in self.__getDictOfBigrams(mainOpinionsCorpus)[airline]]
            fullString = ' '.join(listOfBigrams)
            dataDictParsedFromDictOfBigrams[airline] = fullString
        return dataDictParsedFromDictOfBigrams


    def __getDictOfBigrams(self, mainOpinionsCorpus):
        dictOfBigrams = {}
        for airline in PathsManager().LIST_OF_AIRLINES:
            dictOfBigrams[airline] = ngrams(mainOpinionsCorpus.opinions[airline].split(), 2)
        return dictOfBigrams



