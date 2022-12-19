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
#disable removing special signs in countvectoriser
# countVectoriser = CountVectorizer(token_pattern = '[a-zA-Z0-9$&+,:;=?@#|<>.^*()%!-]+')
vectoriser = CountVectorizer()

downloadedAircraftData = dataDictManager.getDataDictFromFiles(pathsManager.DOWNLOADED_FILES_DIR, 'Aircraft')

mapOfclearedDownloadedAircraftStrings = {}
for airline in airlines:
    mapOfclearedDownloadedAircraftStrings[airline] = downloadedAircraftData[airline]\
        .replace(' ', '').replace('None\n', '').replace('\n', ' ').lower()

# print(mapOfclearedDownloadedAircraftStrings)

mapOfClearedDownloadedAircraftsLists = {}
for airline in airlines:
    mapOfClearedDownloadedAircraftsLists[airline] = mapOfclearedDownloadedAircraftStrings[airline].split(' ')

print(mapOfClearedDownloadedAircraftsLists)

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

print(dictOfListOfTermsToRemove)

finalDict = {}
for airline in airlines:
    helperList = []
    for word in mapOfRegexedAircraftsLists[airline]:
        if not word in dictOfListOfTermsToRemove[airline]:
            helperList.append(word)
    finalDict[airline] = helperList
#
# print(mapOfClearedDownloadedAircraftsLists)

wordsAndCountsDict = {}
for airline in airlines:
    wordsAndCountsDict[airline] = pd.value_counts(np.array(finalDict[airline]))

# print(mapOfWordsAndCounts)

allCount = sum(wordsAndCountsDict['lufthansa'])
df = pd.DataFrame.from_dict(wordsAndCountsDict['lufthansa'])
df.columns=['count']
percentage = [str(round((count/allCount)*100,3)) +'%' for count in wordsAndCountsDict['lufthansa']]
df.insert(1,"percentage",percentage,True)

print(df)
print('#######################################################')
allCount = sum(wordsAndCountsDict['ryanair'])
df1 = pd.DataFrame.from_dict(wordsAndCountsDict['ryanair'])
df1.columns=['count']
percentage = [str(round((count/allCount)*100,3)) +'%' for count in wordsAndCountsDict['ryanair']]
df1.insert(1,"percentage",percentage,True)

print(df1)
print('#######################################################')
allCount = sum(wordsAndCountsDict['wizz-air'])
df2 = pd.DataFrame.from_dict(wordsAndCountsDict['wizz-air'])
df2.columns=['count']
percentage = [str(round((count/allCount)*100,3)) +'%' for count in wordsAndCountsDict['wizz-air']]
df2.insert(1,"percentage",percentage,True)

print(df2)
print('#######################################################')
# #jak to kuźwa przeanalizować?
# #Napisać do Rizun