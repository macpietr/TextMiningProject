from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.FileWriter import FileWriter
from matthausITberatung.objectsManager.PathsManager import PathsManager


downloadedFolder = PathsManager().DOWNLOADED_FILES_DIR()
saveFolder = PathsManager().CLEANED_DATA_FILES_DIR()
mainUserOpinionChildDir = 'MainUserOpinion'
mainMarkInOpinionDir = 'MainMarkInOpinion'

#Clean data for MainUserOpinion
for airline in PathsManager().LIST_OF_AIRLINES():
    downloadedData = FileReader().readFile(downloadedFolder, mainUserOpinionChildDir, airline)
    cleanedData = DataCleaner().cleanDataExtended(downloadedData)
    FileWriter(saveFolder, mainUserOpinionChildDir, airline).putDataIntoFile(cleanedData)

#Clean data for MainMarkInOpinion
for airline in PathsManager().LIST_OF_AIRLINES():
    downloadedData = FileReader().readFile(downloadedFolder, mainMarkInOpinionDir, airline)
    cleanedData = DataCleaner().cleanData(downloadedData)
    FileWriter(saveFolder, mainMarkInOpinionDir, airline).putDataIntoFile(cleanedData)