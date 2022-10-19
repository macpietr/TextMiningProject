import pandas
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager

pathsManager = PathsManager()
dataDictManager = DataDictManager()
airlines = pathsManager.LIST_OF_AIRLINES

dictOfRecommendedStrings = dataDictManager.getDataDictFromFiles(pathsManager.DOWNLOADED_FILES_DIR, 'IsRecommended')

dictOfRecommendedLists = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dictOfRecommendedLists[airline] = dictOfRecommendedStrings[airline].split('\n')

listOfNoAnswersCount = [dictOfRecommendedLists[airline].count('no') for airline in pathsManager.LIST_OF_AIRLINES]
listOfYesAnswersCount = [dictOfRecommendedLists[airline].count('yes') for airline in pathsManager.LIST_OF_AIRLINES]
listOfCounts = [len(dictOfRecommendedLists[airline])-1 for airline in pathsManager.LIST_OF_AIRLINES]
listOfNoPercentage = [round(listOfNoAnswersCount[i]/listOfCounts[i]*100,2) for i in range(3)]
listOfYesPercentage = [round(listOfYesAnswersCount[i]/listOfCounts[i]*100,2) for i in range(3)]

data = {'NO':listOfNoAnswersCount,
        'YES':listOfYesAnswersCount,
        'NO (%)': listOfNoPercentage,
        'YES (%)': listOfYesPercentage,
        'total':listOfCounts}

df = pandas.DataFrame(data, index=pathsManager.LIST_OF_AIRLINES)

print(df)
