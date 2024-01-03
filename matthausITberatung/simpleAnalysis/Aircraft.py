import re

from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd

pathsManager = PathsManager()
dataDictManager = DataDictManager()
corpusManager = CorpusManager()
dtmManager = DataTermMatrixManager()
airlines = PathsManager().LIST_OF_AIRLINES
vectoriser = CountVectorizer()

downloadedAircraftData = dataDictManager.getDataDictFromFiles(pathsManager.DOWNLOADED_FILES_DIR, 'Aircraft')

mapOfclearedDownloadedAircraftStrings = {}
for airline in airlines:
    mapOfclearedDownloadedAircraftStrings[airline] = downloadedAircraftData[airline]\
        .replace(' ', '').replace('None\n', '').replace('\n', ' ').lower()


mapOfClearedDownloadedAircraftsLists = {}
for airline in airlines:
    mapOfClearedDownloadedAircraftsLists[airline] = mapOfclearedDownloadedAircraftStrings[airline].split(' ')

# clean names of aircraft models
mapOfRegexedAircraftsLists = {}
for airline in airlines:
    helperList = []
    for value in mapOfClearedDownloadedAircraftsLists[airline]:
        if value[:1] == "a":
            value = "a" + re.sub("[^0-9]", "", value)[:3]
        else:
            value = re.sub("[^0-9]", "", value)[:3]
        if len(value) > 2:
            helperList.append(value)
    mapOfRegexedAircraftsLists[airline] = helperList

print(mapOfRegexedAircraftsLists)

wordsAndCountsDict = {}
for airline in airlines:
    wordsAndCountsDict[airline] = pd.value_counts(np.array(mapOfRegexedAircraftsLists[airline]))

dictOfListOfTermsToRemove = {}
for airline in airlines:
    listOfTermsToRemove = []
    for word in wordsAndCountsDict[airline].keys():
        if wordsAndCountsDict[airline][word] == 1:
            listOfTermsToRemove.append(word)
    dictOfListOfTermsToRemove[airline] = listOfTermsToRemove

finalDict = {}
for airline in airlines:
    helperList = []
    for word in mapOfRegexedAircraftsLists[airline]:
        if not word in dictOfListOfTermsToRemove[airline]:
            helperList.append(word)
    finalDict[airline] = helperList

wordsAndCountsDict = {}
for airline in airlines:
    wordsAndCountsDict[airline] = pd.value_counts(np.array(finalDict[airline]))

for airline in airlines:
    allCount = sum(wordsAndCountsDict[airline])
    df = pd.DataFrame.from_dict(wordsAndCountsDict[airline])
    df.columns=['count']
    percentage = [str(round((count/allCount)*100,3)) +'%' for count in wordsAndCountsDict[airline]]
    df.insert(1,"percentage",percentage,True)

    print(airline)
    print(df)
    print('#######################################################')