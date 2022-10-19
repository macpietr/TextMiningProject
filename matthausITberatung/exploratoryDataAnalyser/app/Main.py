from collections import Counter

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer

from matthausITberatung.exploratoryDataAnalyser.analyser.BigramsManager import BigramsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager
from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.exploratoryDataAnalyser.analyser.TopWordsDictManager import TopWordsDictManager
from matthausITberatung.exploratoryDataAnalyser.analyser.SummaryTableManager import SummaryTableManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.stopWords.manager.StopWordsManager import StopWordsManager


##BASIC PART
#Create objects which are managers for certain operations
pathsManager = PathsManager()
dataDictManager = DataDictManager()
corpusManager = CorpusManager()
dataTermMatrixManager = DataTermMatrixManager()
objectManager = ObjectsManager()
topWordsDictManager = TopWordsDictManager()
stopWordsManager = StopWordsManager()
summaryTableManager = SummaryTableManager()
bigramsManager = BigramsManager()

POTENTIAL_STOP_WORDS_LIST = objectManager.getSavedObject(pathsManager.POTENTIAL_STOP_WORDS_LIST)
STOP_WORDS_LIST_FROM_SHORT_WORDS = objectManager.getSavedObject(pathsManager.STOP_WORDS_LIST_FROM_SHORT_WORDS)

#TODO: Remember to check behaviuor with and without POTENTIAL_STOP_WORDS_LIST. Especially in wordClouds
UNION_STOP_WORDS = text.ENGLISH_STOP_WORDS.union(POTENTIAL_STOP_WORDS_LIST).union(STOP_WORDS_LIST_FROM_SHORT_WORDS)
#CountVectorizer will be required object to create DTM
#It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text.
countVectorizer = CountVectorizer(stop_words=UNION_STOP_WORDS)
objectManager.saveObject(countVectorizer, 'countVectorizer')

#Prepare dict of cleand data for every airline
cleanedDataDict = dataDictManager.getDataDictFromFiles(PathsManager().CLEANED_DATA_FILES_DIR, partOfScrappedData='MainUserOpinion')
cleandDataDictForCorpus = dataDictManager.getDataDictForCorpus(cleanedDataDict)
lemmitizedDataDict = dataDictManager.getLemmatizedDataDictForCorpus(cleandDataDictForCorpus)
dataDictWithoutStopWords = dataDictManager.getDataDictWithoutStopWords(lemmitizedDataDict, UNION_STOP_WORDS)

#We have to create corpus

#1 corpus with stop words included - only for display purpose
mainOpinionsCorpus = corpusManager.createCorpus(cleandDataDictForCorpus, 100)
mainOpinionsCorpus.columns = ['opinions']
print('###### Display Corpus #######')
print(mainOpinionsCorpus)
print('#############################')
print('')

#2 corpus without stop words - for further analysis
mainOpinionsCorpusWithoutStopWords = corpusManager.createCorpus(dataDictWithoutStopWords, 30)
#name columns with opinions from corpus as 'opinions'. We have only one column in our corpus, beacuse airlines are index of corpus
mainOpinionsCorpusWithoutStopWords.columns = ['opinions']

print('########## Display Corpus without stop words ###########')
print(mainOpinionsCorpusWithoutStopWords)
print('#############################')
print('')

#Create DTM basing on previous corpus and countVectorizer which takes stop words into account
mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpusWithoutStopWords.opinions, countVectorizer)

#assign corpus index to DTM index. It replaces numeric index with appropriate airline names brought from corpus
#rows of DTM are labeled as certain arilines.
mainOpinionsDTM.index = mainOpinionsCorpusWithoutStopWords.index

#print(mainOpinionsDTM.columns)
mainOpinionsTDM = mainOpinionsDTM.transpose()
print('######### TDM head(30)')
print(mainOpinionsTDM.head(30))

#Create a dictionary where key is the airline and value is a list of words and their number of appearance (word, count)
airlinesDictOfListsOfWords = dataDictManager.createDataDictOfListsOfWords(dataDictWithoutStopWords)
airlinesDictOfCountedWordsCounter = dataDictManager\
    .createDataDictOfDictsOfCountedWordsWithoutDefaultStopWords(airlinesDictOfListsOfWords,
                                                                countVectorizer.get_stop_words())

#print(topWordsDict)

topWordsDictManager.printTopWords(airlinesDictOfCountedWordsCounter, 12)

#Poniżej wrzucamy 30 najczęściej występujących słów do tablicy words dla każdej lini lotniczej

topCommonWords = topWordsDictManager.getTopCommonWords(airlinesDictOfCountedWordsCounter, 30)

print("####### TOP COMMON WORDS #######")
print(topCommonWords)
print("### length of top common words")
print(len(topWordsDictManager.getTopCommonWords(airlinesDictOfCountedWordsCounter, 30)))
#Dzięki counterowi, możemy wskazać, które słowo z wcześniej wrzuconych powtórzyło się. Otzymujemy słowo i numer w ilu opiniach lini lotniczych wystąpiło
print("###### most common words")
print(Counter(topCommonWords).most_common())
#Możemy zdecydować, które spośród tych słów trafi do stop words, a które będziemy badać
print(len(airlinesDictOfCountedWordsCounter.keys()))
potentialStopWordsList = stopWordsManager.createStopWordsListBasedOnCommonWords(topCommonWords, 3)
print("#### potential stop words list ########")
print(potentialStopWordsList)


summaryTable = summaryTableManager.createSummaryTable(mainOpinionsTDM)

print(UNION_STOP_WORDS)
print(summaryTable)


######## BIGRAMS - repetition of previous steps, but using bigrams data############
dictOfListsOfBigrams = bigramsManager.getDictOfListsOfBigrams(dataDictWithoutStopWords)

print('#################### BIGRAMS dataDictParsedFromDictOfBigrams')
print(dictOfListsOfBigrams.keys())
print('#################')


######## clean the dictOfListsOfBigrams #####
for key in dictOfListsOfBigrams.keys():
    dictOfListsOfBigrams[key] = [word.replace('online checkin', 'check online') for word in dictOfListsOfBigrams[key]]
    dictOfListsOfBigrams[key] = [word.replace('online check', 'check online') for word in dictOfListsOfBigrams[key]]
    dictOfListsOfBigrams[key] = [word.replace('checkin online', 'check online') for word in dictOfListsOfBigrams[key]]

##### create dicOfCounters - this is the dict where key is a word and value is the frequency of times this word appeared
dictOfCountersFromBigrams = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dictOfCountersFromBigrams[airline] = Counter(dictOfListsOfBigrams[airline])

objectManager.saveObject(mainOpinionsCorpusWithoutStopWords, pathsManager.MAIN_OPINIONS_CORPUS_WITHOUT_STOPWORDS)
objectManager.saveObject(UNION_STOP_WORDS, pathsManager.UNION_STOP_WORDS)
objectManager.saveObject(airlinesDictOfCountedWordsCounter, pathsManager.AIRLINES_DICT_OF_COUNTED_WORDS_COUNTER)
objectManager.saveObject(mainOpinionsTDM, pathsManager.MAIN_OPINIONS_TDM)
objectManager.saveObject(summaryTable, pathsManager.SUMMARY_TABLE)
objectManager.saveObject(dictOfListsOfBigrams, pathsManager.DICT_LIST_OF_BIGRAMS)
objectManager.saveObject(dictOfCountersFromBigrams, pathsManager.DICT_OF_COUNTERS_FROM_BIGRAMS)
objectManager.saveObject(dataDictWithoutStopWords, pathsManager.DATA_DICT_WITHOUT_STOP_WORDS)