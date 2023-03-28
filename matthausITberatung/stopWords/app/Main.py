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
NUMBER_OF_TOP_WORDS_PER_AIRLINE = 30
NUMBER_OF_DOCUMENTS_IN_WHICH_WORDS_OCCURED = 3

countVectorizer = CountVectorizer(stop_words='english')
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

airlinesDataDictFromFiles = dataDictManager.getDataDictFromFiles(PathsManager().CLEANED_DATA_FILES_DIR, partOfScrappedData='MainUserOpinion')
airlinesDataDictOfLists = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    airlinesDataDictOfLists[airline] = airlinesDataDictFromFiles[airline].split('\n')

lemmatizedAirlinesDataDictOfLists = dataDictManager.getLemmatizedDataDictOfLists(airlinesDataDictOfLists)

airlinesDataDictForCorpus = {}
lemmatizedAirlinesDataDictForCorpus = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    airlinesDataDictForCorpus[airline] = ' '.join(airlinesDataDictOfLists[airline])
    lemmatizedAirlinesDataDictForCorpus[airline] = ' '.join(lemmatizedAirlinesDataDictOfLists[airline])

mainOpinionsCorpus = corpusManager.createCorpus(lemmatizedAirlinesDataDictForCorpus, 30)
mainOpinionsCorpus.columns = ['opinions']
mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions, countVectorizer)
mainOpinionsDTM.index = mainOpinionsCorpus.index

print(mainOpinionsDTM)


airlinesDictOfCountedWordsWithoutStopWords = dataDictManager\
    .createDataDictOfDictsOfCountedWordsWithoutDefaultStopWords(lemmatizedAirlinesDataDictOfLists,
                                                                countVectorizer.get_stop_words())

topCommonWords = topWordsDictManager.getTopCommonWords(airlinesDictOfCountedWordsWithoutStopWords, NUMBER_OF_TOP_WORDS_PER_AIRLINE)
potentialStopWordsList = stopWordsManager.createStopWordsListBasedOnCommonWords(topCommonWords,
                                                                                NUMBER_OF_DOCUMENTS_IN_WHICH_WORDS_OCCURED)

stopWordsListFromShortWords = stopWordsManager.createStopWordsListFromShortWords(lemmatizedAirlinesDataDictForCorpus, 3)

objectManager.saveObject(stopWordsListFromShortWords, pathsManager.STOP_WORDS_LIST_FROM_SHORT_WORDS)
objectManager.saveObject(potentialStopWordsList, pathsManager.POTENTIAL_STOP_WORDS_LIST)

print(potentialStopWordsList)
