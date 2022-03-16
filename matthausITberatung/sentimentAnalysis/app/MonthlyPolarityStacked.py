from collections import OrderedDict
from datetime import datetime

from matplotlib import pyplot as plt
from textblob import TextBlob

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

from matthausITberatung.sentimentAnalysis.app import MonthlyPolarityPreparation

pathsManager = PathsManager()
objectsManager = ObjectsManager()

dictOfAirlinesOfDateCounters = objectsManager.getSavedObject(pathsManager.DICT_OF_AIRLINES_DATE_COUNTERS)
dictOfListsOfDateAndStringInYear = objectsManager.getSavedObject(pathsManager.DICT_OF_LISTS_OF_DATE_AND_STRING_IN_YEAR)

dictOfAirlinesDictOfDateFlownAndCollectedOpininsInOneYear = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dictOfDateFlownAndCollectedOpininsInOneYear = {}
    for dateFlown in dictOfAirlinesOfDateCounters[airline].keys():
        listOfOpinionsForCertainDateAndAirline = []
        for dateFlownAndOpinion in dictOfListsOfDateAndStringInYear[airline]:
            if str(dateFlownAndOpinion[0]) == str(dateFlown):
                listOfOpinionsForCertainDateAndAirline.append(dateFlownAndOpinion[1])
        convertedDateFlown = datetime.strptime(dateFlown, "%B %Y")
        dictOfDateFlownAndCollectedOpininsInOneYear[convertedDateFlown] = ' '.join(listOfOpinionsForCertainDateAndAirline)
    dictOfAirlinesDictOfDateFlownAndCollectedOpininsInOneYear[airline] = dictOfDateFlownAndCollectedOpininsInOneYear

sortedDictOfAirlinesDictOfDateFlownAndCollectedOpininsInOneYear = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dictOfAirlinesDictOfDateFlownAndCollectedOpininsInOneYear[airline] = \
    OrderedDict(sorted(dictOfAirlinesDictOfDateFlownAndCollectedOpininsInOneYear[airline].items()))
    sortedDictOfDateFlownAndCollectedOpininsInOneYear = {}
    for item in dictOfAirlinesDictOfDateFlownAndCollectedOpininsInOneYear[airline].items():
        newKey = item[0].strftime("%B %Y")
        value = item[1]
        sortedDictOfDateFlownAndCollectedOpininsInOneYear[newKey] = value
    sortedDictOfAirlinesDictOfDateFlownAndCollectedOpininsInOneYear[airline] = sortedDictOfDateFlownAndCollectedOpininsInOneYear

print(sortedDictOfAirlinesDictOfDateFlownAndCollectedOpininsInOneYear[pathsManager.LUFTHANSA])

sortedDictOfAirlinesDictOfDateAndPolarity = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    sortedDictOfDateAndPolarity = {}
    for item in sortedDictOfAirlinesDictOfDateFlownAndCollectedOpininsInOneYear[airline].items():
        sortedDictOfDateAndPolarity[item[0]] = TextBlob(item[1]).sentiment.polarity
    sortedDictOfAirlinesDictOfDateAndPolarity[airline] = sortedDictOfDateAndPolarity

print(sortedDictOfAirlinesDictOfDateAndPolarity[pathsManager.LUFTHANSA].items())

for airline in pathsManager.LIST_OF_AIRLINES:
    plt.plot(sortedDictOfAirlinesDictOfDateAndPolarity[airline].keys(), sortedDictOfAirlinesDictOfDateAndPolarity[airline].values())
    plt.axhline(y=0.0, color='r', linestyle='-')
    plt.title(airline)
    plt.ylim(ymin=-1,ymax=1)
    plt.xticks(rotation=45)
    plt.show()