from collections import OrderedDict
from datetime import datetime

from matplotlib import pyplot as plt
from textblob import TextBlob

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

pathsManager = PathsManager()
objectsManager = ObjectsManager()

dictOfAirlinesOfDateCounters = objectsManager.getSavedObject(pathsManager.DICT_OF_AIRLINES_DATE_COUNTERS)
dictOfListsOfDateAndStringInYear = objectsManager.getSavedObject(pathsManager.DICT_OF_LISTS_OF_DATE_AND_STRING_IN_YEAR)

dictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dictOfDateFlownAndAveragePolarityInOneYear = {}
    for dateFlown in dictOfAirlinesOfDateCounters[airline].keys():
        listOfPolarityOfOpinionsForCertainDateAndAirline = []
        for dateFlownAndOpinion in dictOfListsOfDateAndStringInYear[airline]:
            if str(dateFlownAndOpinion[0]) == str(dateFlown):
                listOfPolarityOfOpinionsForCertainDateAndAirline.append(TextBlob(dateFlownAndOpinion[1]).sentiment.polarity)
        avgPolarityForCertainDate = sum(listOfPolarityOfOpinionsForCertainDateAndAirline)/len(listOfPolarityOfOpinionsForCertainDateAndAirline)
        convertedDateFlown = datetime.strptime(dateFlown, "%B %Y")
        dictOfDateFlownAndAveragePolarityInOneYear[convertedDateFlown] = avgPolarityForCertainDate
    dictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear[airline] = dictOfDateFlownAndAveragePolarityInOneYear

sortedDictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear[airline] = \
    OrderedDict(sorted(dictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear[airline].items()))
    sortedDictOfDateFlownAndAvgPolarityInOneYear = {}
    for item in dictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear[airline].items():
        newKey = item[0].strftime("%B %Y")
        value = item[1]
        sortedDictOfDateFlownAndAvgPolarityInOneYear[newKey] = value
    sortedDictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear[airline] = sortedDictOfDateFlownAndAvgPolarityInOneYear

for item in sortedDictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear[pathsManager.LUFTHANSA].items():
    print(item)


for airline in pathsManager.LIST_OF_AIRLINES:
    plt.plot(sortedDictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear[airline].keys(), sortedDictOfAirlinesAndDictOfDateFlownAndAvgPolarityInOneYear[airline].values())
    plt.show()