import pandas
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager

# toPattern = ' to '
# viaPattern = ' via '
# amperPattern = ' & '
# listOfItems = []
# item = 'Venice to San Francisco via Munich'
# toPosition = item.find(toPattern)
# listOfItems.append(item[:toPosition])
# print(listOfItems)
# viaPosition = item.find(viaPattern)
# listOfItems.append(item[len(listOfItems[0]+toPattern):viaPosition])
# print(listOfItems)
# listOfItems.append(item[len(listOfItems[0]+toPattern+listOfItems[1]+viaPattern):])
# print(listOfItems)

pathsManager = PathsManager()
dataDictManager = DataDictManager()
airlines = pathsManager.LIST_OF_AIRLINES

dictOfRouteStrings = dataDictManager.getDataDictFromFiles(pathsManager.DOWNLOADED_FILES_DIR, 'Route')



dictOfRouteLists = {}
for airline in airlines:
    dictOfRouteLists[airline] = dictOfRouteStrings[airline].split('\n')


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

print(dictOfCleanedLists)


