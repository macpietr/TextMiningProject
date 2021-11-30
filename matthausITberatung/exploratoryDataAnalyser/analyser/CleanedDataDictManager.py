from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.PathsManager import PathsManager


class CleanedDataDictManager:

    def getDataDictForCorpus(self, dataDict):
        return {key: [dataDict[key]] for (key, value) in dataDict.items()}

    def getCleanedDataDictFromFiles(self, partOfScrappedData):
        cleanedDataDict = {}
        for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES):
            cleanedDataDict[airline] = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR, partOfScrappedData, airline)
        return cleanedDataDict
