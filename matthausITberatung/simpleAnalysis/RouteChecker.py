import numpy as np
import pandas
import pandas as pd

from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager

pathsManager = PathsManager()
dataDictManager = DataDictManager()
airlines = pathsManager.LIST_OF_AIRLINES

dictOfRouteStrings = dataDictManager.getDataDictFromFiles(pathsManager.DOWNLOADED_FILES_DIR, 'Route')

dictOfRouteLists = {}
for airline in airlines:
    dictOfRouteLists[airline] = dictOfRouteStrings[airline].split('\n')

# adjust routes description to matrix
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

# Check variety of routes
# split journey changes to separate routes
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

# calculate number of distinct routes
dictOfParsedRoutesSetOfString = {}
for airline in airlines:
    # create set to avoid duplicates
    parsedRoutesSetOfString = set()
    for item in dictOfParsedRoutes[airline]:
        #to allow items to be appended to set, they need to be hashable like i.e. strings
        parsedRoutesSetOfString.add(
            str(item).replace('\'', '').replace('[', '').replace(']', '').rstrip().lstrip()
        )
    dictOfParsedRoutesSetOfString[airline] = list(parsedRoutesSetOfString)

listOfSize = []
[listOfSize.append(len(dictOfParsedRoutesSetOfString[airline])) for airline in airlines]

print(listOfSize)

data = {'Number of distinct routes':listOfSize}
df = pandas.DataFrame(data, index=airlines)

print(df)

## check most common airports
dictOfSeparateAirports = {}
for airline in airlines:
    #flatMap
    listOfSeparateAirports = []
    for row in dictOfParsedRoutes[airline]:
        for item in row:
            listOfSeparateAirports.append(item)
    dictOfSeparateAirports[airline] = listOfSeparateAirports

print(dictOfSeparateAirports)

airportsAndCountsDict = {}
for airline in airlines:
    airportsAndCountsDict[airline] = pandas.value_counts(np.array(dictOfSeparateAirports[airline]))
    allCount = sum(airportsAndCountsDict[airline])
    df = pd.DataFrame.from_dict(airportsAndCountsDict[airline])
    df.columns=['count']
    percentage = [str(round((count / allCount) * 100, 3)) + '%' for count in airportsAndCountsDict[airline]]
    df.insert(1, "sum", allCount, True)
    df.insert(2, "percentage", percentage, True)
    print(airline)
    print(df)
    print('#######################################################')


dictOfSeparateDistinctAirports = {}
for airline in airlines:
    dictOfSeparateDistinctAirports[airline] = set(dictOfSeparateAirports[airline])

listOfDistinctAirportsCounts = []
[listOfDistinctAirportsCounts.append(len(dictOfSeparateDistinctAirports[airline])) for airline in airlines]

data = {'Number of distinct airports':listOfDistinctAirportsCounts}
df = pandas.DataFrame(data, index=airlines)

print(df)