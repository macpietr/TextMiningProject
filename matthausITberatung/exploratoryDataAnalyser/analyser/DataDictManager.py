from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.PathsManager import PathsManager


class CleanedDataDictManager:

    def getDataDictForCorpus(self, dataDict):
        return {key: [dataDict[key]] for (key, value) in dataDict.items()}

    def getDataDictFromFiles(self, partOfScrappedData):
        cleanedDataDict = {}
        for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES):
            cleanedDataDict[airline] = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR, partOfScrappedData, airline)
        return cleanedDataDict

    def getcleandDataDictForCorpusWithoutStopWords(self, dataDict, stopWords):
        cleandDataDictForCorpusWithoutStopWords = {}
        for key in dataDict.keys():
            airlineList = []
            for opinion in dataDict[key]:
                for word in opinion.split(" "):
                    if (word.strip() not in stopWords):
                        airlineList.append(word)
            cleandDataDictForCorpusWithoutStopWords[key] = ' '.join(airlineList)
