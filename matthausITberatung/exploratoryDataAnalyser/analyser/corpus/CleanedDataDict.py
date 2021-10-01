from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.fileManager.FileReader import FileReader
from matthausITberatung.fileManager.PathsManager import PathsManager

class CleanedDataDict:


    def getCleanedDataDictForCorpus(self):
        cleanedDataDict = self.getCleanedDataDict()
        return {key: [cleanedDataDict[key]] for (key, value) in cleanedDataDict.items()}

    def getCleanedDataDict(self):
        cleanedDataDict = {}
        for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES()):
            downloadedData = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR(), 'MainUserOpinion', airline)
            cleanedDataDict[airline] = DataCleaner().cleanData(downloadedData)
        return cleanedDataDict