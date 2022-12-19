import numpy
import pandas
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager

pathsManager = PathsManager()
dataDictManager = DataDictManager()
airlines = pathsManager.LIST_OF_AIRLINES

dictOfRouteStrings = dataDictManager.getDataDictFromFiles(pathsManager.DOWNLOADED_FILES_DIR, 'Route')



dictOfRouteLists = {}
for airline in airlines:
    dictOfRouteLists[airline] = dictOfRouteStrings[airline].split('\n')

print(dictOfRouteLists['wizz-air'])

toPattern = ' to '
viaPattern = ' via '
amperPattern = ' & '
dictOfCleanedLists = {}
for airline in airlines:
    cleanedList = []
    for item in dictOfRouteLists[airline]:
        item.replace('  ',' ')
        listOfItems = []
        toPosition = item.find(toPattern)
        viaPosition = item.find(viaPattern)
        amperPosition = item.find(amperPattern)
        if amperPattern in item:
            listOfItems.append(item[:toPosition])
            listOfItems.append(item[len(listOfItems[0] + toPattern):viaPosition])
            listOfItems.append(item[len(listOfItems[0] + toPattern + listOfItems[1] + viaPattern):amperPosition])
            listOfItems.append(item[len(listOfItems[0] + toPattern + listOfItems[1] + viaPattern + listOfItems[2] + amperPattern):])
        elif viaPattern in item:
            listOfItems.append(item[:toPosition])
            listOfItems.append(item[len(listOfItems[0] + toPattern):viaPosition])
            listOfItems.append(item[len(listOfItems[0] + toPattern + listOfItems[1] + viaPattern):])
        elif toPattern in item:
            listOfItems.append(item[:toPosition])
            listOfItems.append(item[len(listOfItems[0] + toPattern):])
        cleanedList.append(listOfItems)
    dictOfCleanedLists[airline] = cleanedList

print(dictOfCleanedLists['wizz-air'])

dictOfParsedRoutes = {}
for airline in airlines:
    parsedRoutesList = []
    for item in dictOfCleanedLists[airline]:
        if len(item) == 4:
            parsedRoutesList.append([item[0], item[2]])
            parsedRoutesList.append([item[2], item[3]])
            parsedRoutesList.append([item[3], item[1]])
        if len(item) == 3:
            parsedRoutesList.append([item[0], item[2]])
            parsedRoutesList.append([item[2], item[1]])
        if len(item) == 2:
            parsedRoutesList.append(item)
    dictOfParsedRoutes[airline] = parsedRoutesList

counts = pandas.value_counts(dictOfParsedRoutes['ryanair'])

print(counts)