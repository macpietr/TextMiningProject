from collections import Counter

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer

from matthausITberatung.exploratoryDataAnalyser.analyser.BigramsManager import BigramsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.CleanedDataDictManager import CleanedDataDictManager
from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.exploratoryDataAnalyser.analyser.TopWordsDictManager import TopWordsDictManager
from matthausITberatung.exploratoryDataAnalyser.analyser.SummaryTableManager import SummaryTableManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.stopWords.manager.StopWordsManager import StopWordsManager


##BASIC PART
#Create objects which are managers for certain operations
corpusManager = CorpusManager()
dataTermMatrixManager = DataTermMatrixManager()
objectManager = ObjectsManager()
topWordsDictManager = TopWordsDictManager()
stopWordsManager = StopWordsManager()
summaryTableManager = SummaryTableManager()
bigramsManager = BigramsManager()

POTENTIAL_STOP_WORDS_LIST = objectManager.getSavedObject('potentialStopWordsList')
UNION_STOP_WORDS = text.ENGLISH_STOP_WORDS.union(POTENTIAL_STOP_WORDS_LIST)
#CountVectorizer will be required object to create DTM
#It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text.
countVectorizer = CountVectorizer(stop_words=UNION_STOP_WORDS)
objectManager.saveObject(countVectorizer, 'countVectorizer')

#Prepare dict of cleand data for every airline
cleanedDataDict = CleanedDataDictManager().getCleanedDataDictFromFiles(partOfScrappedData='MainUserOpinion')
cleandDataDictForCorpus = CleanedDataDictManager().getDataDictForCorpus(cleanedDataDict)
#We have to create corpus
mainOpinionsCorpus = corpusManager.createCorpus(cleandDataDictForCorpus, 30)

print(mainOpinionsCorpus)

#name columns with opinions from corpus as 'opinions'. We have only one column in our corpus, beacuse airlines are index of corpus
mainOpinionsCorpus.columns = ['opinions']

#Create DTM basing on previous corpus and countVectorizer which takes stop words into account
mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions, countVectorizer)

#assign corpus index to DTM index. It replaces numeric index with appropriate airline names brought from corpus
#rows of DTM are labeled as certain arilines.
mainOpinionsDTM.index = mainOpinionsCorpus.index

#print(mainOpinionsDTM.columns)
mainOpinionsTDM = mainOpinionsDTM.transpose()
print('######### TDM head(30)')
print(mainOpinionsTDM.head(30))

#Create a dictionary where key is the airline and value is a list of words and their number of appearance (word, count)
topWordsDict = topWordsDictManager.createTopWordsDict(mainOpinionsTDM)

#print(topWordsDict)

topWordsDictManager.printTopWords(topWordsDict,12)

print(topWordsDict["lufthansa"][0:14])



#Poniżej wrzucamy 30 najczęściej występujących słów do tablicy words dla każdej lini lotniczej

topCommonWords = topWordsDictManager.getTopCommonWords(topWordsDict,30)

print("####### TOP COMMON WORDS #######")
print(topCommonWords)
print("### length of top common words")
print(len(topWordsDictManager.getTopCommonWords(topWordsDict,30)))
#Dzięki counterowi, możemy wskazać, które słowo z wcześniej wrzuconych powtórzyło się. Otzymujemy słowo i numer w ilu opiniach lini lotniczych wystąpiło
print("###### mose common word")
print(Counter(topCommonWords).most_common())
#Możemy zdecydować, które spośród tych słów trafi do stop words, a które będziemy badać
print(len(topWordsDict.keys()))
potentialStopWordsList = stopWordsManager.createPotentialStopWordsList(topCommonWords,3)
print("#### potential stop words list ########")
print(potentialStopWordsList)


summaryTable = summaryTableManager.createSummaryTable(mainOpinionsTDM)

print(UNION_STOP_WORDS)
print(summaryTable)


######## BIGRAMS - repetition of previous steps, but using bigrams data############


dataDictParsedFromDictOfBigrams = bigramsManager.getDataDictParsedFromDictOfBigrams(mainOpinionsCorpus)

dictForBigramsCorpus = CleanedDataDictManager().getDataDictForCorpus(dataDictParsedFromDictOfBigrams)

bigramsCorpus = CorpusManager().createCorpus(dictForBigramsCorpus, 30)
bigramsCorpus.columns = ['bigramsOpinions']
bigramsDTM = DataTermMatrixManager().createDataTermMatrix(bigramsCorpus.bigramsOpinions, countVectorizer)
bigramsDTM.index = bigramsCorpus.index

print(bigramsCorpus)
print("########")

bigramsTDM = bigramsDTM.transpose()

bigramsTopWordsDict = TopWordsDictManager().createTopWordsDict(bigramsTDM)

TopWordsDictManager().printTopWords(bigramsTopWordsDict, 12)

topCommonBigramsWords = TopWordsDictManager().getTopCommonWords(bigramsTopWordsDict, 30)

print(topCommonBigramsWords)

bigramsSummaryTable = SummaryTableManager().createSummaryTable(bigramsTDM)

print('##### bigrams summary table #####')
print(bigramsSummaryTable)

objectManager.saveObject(mainOpinionsCorpus, 'mainOpinionsCorpus')
objectManager.saveObject(UNION_STOP_WORDS,'unionStopWords')
objectManager.saveObject(topWordsDict,'topWordsDict')
objectManager.saveObject(bigramsTopWordsDict, 'bigramsTopWordsDict')
objectManager.saveObject(mainOpinionsTDM, 'mainOpinionsTDM')
objectManager.saveObject(bigramsTDM, 'bigramsTDM')
objectManager.saveObject(summaryTable, 'summaryTable')
objectManager.saveObject(bigramsSummaryTable, 'bigramsSummaryTable')
