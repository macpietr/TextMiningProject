from matthausITberatung.dataCleaner.cleaner.GeneralDataCleaner import GeneralDataCleaner
from matthausITberatung.fileManager.FileReader import FileReader
from matthausITberatung.fileManager.FileWriter import FileWriter
from matthausITberatung.fileManager.PathsManager import PathsManager

saveFolder = PathsManager().CLEANED_DATA_FILES_DIR()
downloadedFolder = PathsManager().DOWNLOADED_FILES_DIR()
listOfCasesRequiredCleaning = ['MainUserOpinion','MainMarkInOpinion']

for airlineName in PathsManager().LIST_OF_AIRLINES():
    for case in listOfCasesRequiredCleaning:
        readFile = FileReader().readFile(downloadedFolder, case, airlineName)
        cleanedData = GeneralDataCleaner(readFile).cleanData()
        FileWriter(airlineName, case, saveFolder).putDataIntoFile(cleanedData)