from collections import Counter

from matthausITberatung.objectsManager.CollectionsFromFiles import CollectionsFromFiles
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

YEAR = '2021'

pathsManager = PathsManager()
objectsManager = ObjectsManager()
collectionsFromFiles = CollectionsFromFiles()
airlinesDictOfListsOfMainOpinions = collectionsFromFiles.createDictOfListsOfRecordsFromDownloadedFile('MainUserOpinion')
airlinesDictOfListsOfDateFlown = collectionsFromFiles.createDictOfListsOfRecordsFromDownloadedFile('DateFlown')

dictOfListsOfDateAndString = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    lufthansaListOfMainOpinions = airlinesDictOfListsOfMainOpinions[airline]
    del lufthansaListOfMainOpinions[len(lufthansaListOfMainOpinions)-1]
    lufthansaListOfDateFlown = airlinesDictOfListsOfDateFlown[airline]
    del lufthansaListOfDateFlown[len(lufthansaListOfDateFlown)-1]
    dictOfListsOfDateAndString[airline] = list(zip(lufthansaListOfDateFlown,lufthansaListOfMainOpinions))

dictOfListsOfDateAndStringInYear = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dateAndStringList = []
    for dateAndString in dictOfListsOfDateAndString[airline]:
        if dateAndString[0][len(dateAndString) - 6:] == YEAR:
            dateAndStringList.append(dateAndString)
    dictOfListsOfDateAndStringInYear[airline] = dateAndStringList

dictOfAirlinesOfDateCounters = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    date, string = zip(*dictOfListsOfDateAndStringInYear[airline])
    dictOfAirlinesOfDateCounters[airline] = Counter(date)

objectsManager.saveObject(dictOfAirlinesOfDateCounters,pathsManager.DICT_OF_AIRLINES_DATE_COUNTERS)
objectsManager.saveObject(dictOfListsOfDateAndStringInYear,pathsManager.DICT_OF_LISTS_OF_DATE_AND_STRING_IN_YEAR)