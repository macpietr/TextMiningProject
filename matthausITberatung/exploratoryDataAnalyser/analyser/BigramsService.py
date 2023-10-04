from nltk import ngrams

class BigramsService:

    def getDictOfListsOfBigrams(self, dataDict):
        dataDictParsedFromDictOfBigrams = {}
        for key in dataDict.keys():
            listOfBigrams = [' '.join(bigram) for bigram in ngrams(dataDict[key].split(), 2)]
            dataDictParsedFromDictOfBigrams[key] = listOfBigrams
        return dataDictParsedFromDictOfBigrams