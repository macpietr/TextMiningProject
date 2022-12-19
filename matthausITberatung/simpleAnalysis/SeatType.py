import pandas

from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager

pathsManager = PathsManager()
dataDictManager = DataDictManager()
airlines = pathsManager.LIST_OF_AIRLINES

dictOfSeatTypeStrings = dataDictManager.getDataDictFromFiles(pathsManager.DOWNLOADED_FILES_DIR, 'SeatType')

dictOfSeatTypeLists = {}
for airline in airlines:
    dictOfSeatTypeLists[airline] = dictOfSeatTypeStrings[airline].split('\n')

dictOfCounts = {}
for airline in airlines:
    dictOfCounts[airline] = pandas.value_counts(dictOfSeatTypeLists[airline])

print(dictOfCounts)