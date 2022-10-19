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
print(countVectorizer.get_stop_words())
##BASIC PART
# Create objects which are managers for certain operations
dataDictManager = DataDictManager()
corpusManager = CorpusManager()
dataTermMatrixManager = DataTermMatrixManager()
objectManager = ObjectsManager()
topWordsDictManager = TopWordsDictManager()
stopWordsManager = StopWordsManager()
pathsManager = PathsManager()

airlinesDataDictFromFiles = dataDictManager.getDataDictFromFiles(PathsManager().LIST_OF_AIRLINES, partOfScrappedData='MainUserOpinion')
airlinesDataDictForCorpus = dataDictManager.getDataDictForCorpus(airlinesDataDictFromFiles)
airlinesDataDictOfLemmitizedWords = dataDictManager.getLemmatizedDataDictForCorpus(airlinesDataDictForCorpus)

mainOpinionsCorpus = corpusManager.createCorpus(airlinesDataDictOfLemmitizedWords, 30)
mainOpinionsCorpus.columns = ['opinions']
mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions, countVectorizer)
mainOpinionsDTM.index = mainOpinionsCorpus.index

print(mainOpinionsDTM)

airlinesDataDictOfListsOfLemmatizedWords = dataDictManager.createDataDictOfListsOfWords(airlinesDataDictOfLemmitizedWords)

airlinesDictOfCountedWordsWithoutStopWords = dataDictManager\
    .createDataDictOfDictsOfCountedWordsWithoutDefaultStopWords(airlinesDataDictOfListsOfLemmatizedWords,
                                                                countVectorizer.get_stop_words())

topCommonWords = topWordsDictManager.getTopCommonWords(airlinesDictOfCountedWordsWithoutStopWords, NUMBER_OF_TOP_WORDS_PER_AIRLINE)
potentialStopWordsList = stopWordsManager.createStopWordsListBasedOnCommonWords(topCommonWords,
                                                                                NUMBER_OF_DOCUMENTS_IN_WHICH_WORDS_OCCURED)

stopWordsListFromShortWords = stopWordsManager.createStopWordsListFromShortWords(airlinesDataDictOfLemmitizedWords, 3)

objectManager.saveObject(stopWordsListFromShortWords, pathsManager.STOP_WORDS_LIST_FROM_SHORT_WORDS)
objectManager.saveObject(potentialStopWordsList, pathsManager.POTENTIAL_STOP_WORDS_LIST)

print(potentialStopWordsList)
