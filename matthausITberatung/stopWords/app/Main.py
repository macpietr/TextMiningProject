from collections import Counter

from sklearn.feature_extraction.text import CountVectorizer

from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager
from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.exploratoryDataAnalyser.analyser.TopWordsDictManager import TopWordsDictManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.stopWords.manager.StopWordsManager import StopWordsManager

# The aim of this Main script is to make a pickle object which will be the lis containing additional stop_words
# Configuration
LANGUAGE = 'english'
NUMBER_OF_TOP_WORDS_PER_AIRLINE = 30
NUMBER_OF_DOCUMENTS_IN_WHICH_WORDS_OCCURED = 3

countVectorizer = CountVectorizer(stop_words=LANGUAGE)
##BASIC PART
# Create objects which are managers for certain operations
dataDictManager = DataDictManager()
corpusManager = CorpusManager()
dataTermMatrixManager = DataTermMatrixManager()
objectManager = ObjectsManager()
topWordsDictManager = TopWordsDictManager()
stopWordsManager = StopWordsManager()
pathsManager = PathsManager()

dataDictFromFiles = dataDictManager.getDataDictFromFiles(partOfScrappedData='MainUserOpinion')
dataDictForCorpus = dataDictManager.getDataDictForCorpus(dataDictFromFiles)

stopWordsListFromShortWords = stopWordsManager.createStopWordsListFromShortWords(dataDictForCorpus,3)

mainOpinionsCorpus = corpusManager.createCorpus(dataDictForCorpus, 30)
mainOpinionsCorpus.columns = ['opinions']
mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions, countVectorizer)
mainOpinionsDTM.index = mainOpinionsCorpus.index
topWordsDict = topWordsDictManager.createTopWordsDict(mainOpinionsDTM.transpose())
topCommonWords = topWordsDictManager.getTopCommonWords(topWordsDict, NUMBER_OF_TOP_WORDS_PER_AIRLINE)
potentialStopWordsList = stopWordsManager.createStopWordsListBasedOnCommonWords(topCommonWords,
                                                                                NUMBER_OF_DOCUMENTS_IN_WHICH_WORDS_OCCURED)

objectManager.saveObject(stopWordsListFromShortWords, pathsManager.STOP_WORDS_LIST_FROM_SHORT_WORDS)
objectManager.saveObject(potentialStopWordsList, pathsManager.POTENTIAL_STOP_WORDS_LIST)

print(potentialStopWordsList)
