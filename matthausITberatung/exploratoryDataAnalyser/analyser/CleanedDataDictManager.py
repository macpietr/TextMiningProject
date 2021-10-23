from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.PathsManager import PathsManager


class CleanedDataDictManager:

    def getCleanedDataDictForCorpus(self, partOfScrappedData):
        cleanedDataDict = self.getCleanedDataDict(partOfScrappedData)
        return {key: [cleanedDataDict[key]] for (key, value) in cleanedDataDict.items()}

    def getCleanedDataDict(self, partOfScrappedData):
        cleanedDataDict = {}
        for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES()):
            cleanedDataDict[airline] = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR(), partOfScrappedData, airline)
        return cleanedDataDict
