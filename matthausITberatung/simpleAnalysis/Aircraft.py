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

print(mapOfclearedDownloadedAircraftStrings)

mapOfClearedDownloadedAircraftsLists = {}
for airline in airlines:
    mapOfClearedDownloadedAircraftsLists[airline] = mapOfclearedDownloadedAircraftStrings[airline].split(' ')

print(mapOfClearedDownloadedAircraftsLists)

mapOfWordsAndCounts = {}
for airline in airlines:
    mapOfWordsAndCounts[airline] = pd.value_counts(np.array(mapOfClearedDownloadedAircraftsLists[airline]))

mapOfListOfTermsToRemove = {}
for airline in airlines:
    listOfTermsToRemove = []
    for word in mapOfWordsAndCounts[airline].keys():
        if mapOfWordsAndCounts[airline][word] == 1:
            listOfTermsToRemove.append(word)
    mapOfListOfTermsToRemove[airline] = listOfTermsToRemove

print(mapOfListOfTermsToRemove)

finalMap = {}
for airline in airlines:
    helperList = []
    for word in mapOfClearedDownloadedAircraftsLists[airline]:
        if not word in mapOfListOfTermsToRemove[airline]:
            helperList.append(word)
    finalMap[airline] = helperList

print(mapOfClearedDownloadedAircraftsLists)

mapOfWordsAndCounts = {}
for airline in airlines:
    mapOfWordsAndCounts[airline] = pd.value_counts(np.array(finalMap[airline]))

print(mapOfWordsAndCounts)

allCount = sum(mapOfWordsAndCounts['lufthansa'])
df = pd.DataFrame.from_dict(mapOfWordsAndCounts['lufthansa'])
df.columns=['count']
percentage = [round(count/allCount,3) for count in mapOfWordsAndCounts['lufthansa']]
df.insert(1,"percentage",percentage,True)

print(df)

allCount = sum(mapOfWordsAndCounts['ryanair'])
df1 = pd.DataFrame.from_dict(mapOfWordsAndCounts['ryanair'])
df1.columns=['count']
percentage = [round(count/allCount,3) for count in mapOfWordsAndCounts['ryanair']]
df1.insert(1,"percentage",percentage,True)

print(df1)

allCount = sum(mapOfWordsAndCounts['wizz-air'])
df2 = pd.DataFrame.from_dict(mapOfWordsAndCounts['wizz-air'])
df2.columns=['count']
percentage = [round(count/allCount,3) for count in mapOfWordsAndCounts['wizz-air']]
df2.insert(1,"percentage",percentage,True)

print(df2)

#jak to kuźwa przeanalizować?
#Napisać do Rizun