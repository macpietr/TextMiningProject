import statistics

import pandas as pd
from nltk import bigrams
from sklearn.feature_extraction.text import CountVectorizer

from matthausITberatung.exploratoryDataAnalyser.analyser.BigramsService import BigramsService
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager
from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.exploratoryDataAnalyser.analyser.TopWordsDictManager import TopWordsDictManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.stopWords.manager.StopWordsManager import StopWordsManager


##BASIC PART
#Create objects which are managers for certain operations
from matthausITberatung.stopWords.service.StopWordsService import StopWordsService

pathsManager = PathsManager()
dataDictManager = DataDictManager()
corpusManager = CorpusManager()
dataTermMatrixManager = DataTermMatrixManager()
objectManager = ObjectsManager()
topWordsDictManager = TopWordsDictManager()
stopWordsManager = StopWordsManager()
stopWordsService = StopWordsService()
bigramsService = BigramsService()

UNION_STOP_WORDS = objectManager.getSavedObject(pathsManager.UNION_STOP_WORDS)

countVectorizer = CountVectorizer(stop_words=UNION_STOP_WORDS)

cleanedDataDict = dataDictManager.getDataDictFromFiles(PathsManager().CLEANED_DATA_FILES_DIR, partOfScrappedData='MainUserOpinion')
# cleanedDataDict = dataDictManager.getDataDictFromFiles(PathsManager().CLEANED_DATA_FILES_DIR, partOfScrappedData='TitleOfOpinion')

cleanedDataDictOfLists = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    cleanedDataDictOfLists[airline] = cleanedDataDict[airline].split('\n')
lemmatizedDataDictOfLists = dataDictManager.getLemmatizedDataDictOfLists(cleanedDataDictOfLists)

lemmatizedDataDictOfListsWithoutStopWords = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    lemmatizedDataDictOfListsWithoutStopWords[airline] = stopWordsService.remove_stopwords(lemmatizedDataDictOfLists[airline])

objectManager.saveObject(lemmatizedDataDictOfListsWithoutStopWords, 'dataDictOfClearedOpinions')

lemmatizedDataDictForCorpusWithoutStopWords = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    lemmatizedDataDictForCorpusWithoutStopWords[airline] = ' '.join(lemmatizedDataDictOfListsWithoutStopWords[airline])

#Corpus created from lemmatized and cleaned data
mainOpinionsCorpus = corpusManager.createCorpus(lemmatizedDataDictForCorpusWithoutStopWords, 100)
mainOpinionsCorpus.columns = ['opinions']

print(mainOpinionsCorpus)

#Data Term Matrix created from corpus
mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions, countVectorizer)

print(mainOpinionsDTM)

# Print 30 top words for each airline
dictOfListOf30CountedMostCommonWords = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    print(airline)
    print("--------")
    listOfWords = mainOpinionsDTM.loc[airline].nlargest(30)
    print(listOfWords)
    dictOfListOf30CountedMostCommonWords[airline] = listOfWords

# Save this as an object for world cloud purposes
objectManager.saveObject(dictOfListOf30CountedMostCommonWords, pathsManager.DICT_OF_LIST_OF_30_COUNTED_MOST_COMMON_WORDS)

# Unique words
print("Unique words")
countOfUniqueWordsDict = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    countOfUniqueWordsDict[airline] = mainOpinionsDTM.loc[airline].nunique()

countOfUniqueWordsDtm = pd.DataFrame.from_dict(countOfUniqueWordsDict, orient='index', columns=['Count of unique words'])
print(countOfUniqueWordsDtm)

print("Post per words")

dictOfListsOfStatistics = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    listOfCounts = [len(opinion.split()) for opinion in lemmatizedDataDictOfLists[airline]]
    countOfWords = sum(listOfCounts)
    medianOfWords = statistics.median(listOfCounts)
    avgOfWords = statistics.mean(listOfCounts)
    stdevOfWords = statistics.stdev(listOfCounts)
    dictOfListsOfStatistics[airline] = [countOfWords, medianOfWords, avgOfWords, stdevOfWords]

print(dictOfListsOfStatistics)

dtmOfStatistics = pd.DataFrame.from_dict(dictOfListsOfStatistics, orient='index', columns=['count', 'median', 'avg', 'stdev'])

print('########## DTM of statistics ##########')
print(dtmOfStatistics)


##### BIGRAMS ######

dataDictForBigrams = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    helperList = [item.split(' ') for item in lemmatizedDataDictOfListsWithoutStopWords[airline]]
    dataDictForBigrams[airline] = helperList


dataDictOfBigrams = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    bigramList = [list(bigrams(wordsOfOpinionList)) for wordsOfOpinionList in dataDictForBigrams[airline]]
    helperList = []
    for item in bigramList:
        joinedBigrams = [' '.join(bigram) for bigram in item]
        helperList.append(joinedBigrams)
    dataDictOfBigrams[airline] = helperList

dataDictOfBigramsUnderscore = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    helperList = []
    for item in dataDictOfBigrams[airline]:
        item2 = []
        for bigram in item:
            item2.append(bigram.replace(' ','_'))
        helperList.append(item2)
    dataDictOfBigramsUnderscore[airline] = helperList

dictOfBigramedOpinions = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dictOfBigramedOpinions[airline] = [' '.join(item) for item in dataDictOfBigramsUnderscore[airline]]

objectManager.saveObject(dictOfBigramedOpinions, 'dictOfBigramedOpinions')

dataDictOfBigramsUnderscoreForCorpus = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dataDictOfBigramsUnderscoreForCorpus[airline] = " ".join(" ".join(bigram) for bigram in dataDictOfBigramsUnderscore[airline])

bigramsCorpus = corpusManager.createCorpus(dataDictOfBigramsUnderscoreForCorpus, 100)
bigramsCorpus.columns = ['opinions_bigrams']

bigramVectorizer = CountVectorizer()

bigramsDTM = dataTermMatrixManager.createDataTermMatrix(bigramsCorpus.opinions_bigrams, bigramVectorizer)

print(bigramsDTM)

# Print 30 top words for each airline
dictOfListOf30CountedMostCommonBigrams = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    print(airline)
    print("--------")
    listOfWords = bigramsDTM.loc[airline].nlargest(30)
    print(listOfWords)
    dictOfListOf30CountedMostCommonBigrams[airline] = listOfWords

# Save this as an object for world cloud purposes
objectManager.saveObject(dictOfListOf30CountedMostCommonBigrams, pathsManager.DICT_OF_LIST_OF_30_COUNTED_MOST_COMMON_BIGRAMS)

# Unique words
print("Unique bigrams")
countOfUniqueBigramsDict = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    countOfUniqueBigramsDict[airline] = bigramsDTM.loc[airline].nunique()

countOfUniqueBigramsDtm = pd.DataFrame.from_dict(countOfUniqueBigramsDict, orient='index', columns=['Count of unique bigrams'])
print(countOfUniqueBigramsDtm)

dictOfListsOfStatisticsBigrams = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    listOfCounts = [len(opinion) for opinion in dataDictOfBigrams[airline]]
    countOfWords = sum(listOfCounts)
    medianOfWords = statistics.median(listOfCounts)
    avgOfWords = statistics.mean(listOfCounts)
    stdevOfWords = statistics.stdev(listOfCounts)
    dictOfListsOfStatisticsBigrams[airline] = [countOfWords, medianOfWords, avgOfWords, stdevOfWords]

dtmOfStatisticsBigrams = pd.DataFrame.from_dict(dictOfListsOfStatisticsBigrams, orient='index', columns=['count', 'median', 'avg', 'stdev'])

print('####### DTM of statistics - Bigrams ########')
print(dtmOfStatisticsBigrams)