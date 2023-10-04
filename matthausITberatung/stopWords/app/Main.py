from collections import Counter

from sklearn.feature_extraction.text import CountVectorizer

from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager
from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.exploratoryDataAnalyser.analyser.TopWordsDictManager import TopWordsDictManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.stopWords.manager.StopWordsManager import StopWordsManager

# The aim of this Main script is to make a pickle object which will be the list containing additional stop_words
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

countVectorizer = CountVectorizer(stop_words='english')

cleanedDataDict = dataDictManager.getDataDictFromFiles(PathsManager().CLEANED_DATA_FILES_DIR, partOfScrappedData='MainUserOpinion')

cleanedDataDictOfLists = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    cleanedDataDictOfLists[airline] = cleanedDataDict[airline].split('\n')
lemmatizedDataDictOfLists = dataDictManager.getLemmatizedDataDictOfLists(cleanedDataDictOfLists)

lemmatizedDataDictForCorpusWithoutStopWords = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    lemmatizedDataDictForCorpusWithoutStopWords[airline] = ' '.join(lemmatizedDataDictOfLists[airline])

#Corpus created from lemmatized and cleaned data
mainOpinionsCorpus = corpusManager.createCorpus(lemmatizedDataDictForCorpusWithoutStopWords, 100)
mainOpinionsCorpus.columns = ['opinions']

print(mainOpinionsCorpus)

#Data Term Matrix created from corpus
mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions, countVectorizer)

print(mainOpinionsDTM)

mainOpinionsTDM = mainOpinionsDTM.transpose()
mainOpinionsTDM.columns = pathsManager.LIST_OF_AIRLINES

print(mainOpinionsTDM)


#Create dict of airlines and their top 30 words
dictOfTopDicts = {}
for airline in mainOpinionsTDM.columns:
    top = mainOpinionsTDM[airline].sort_values(ascending=False).head(30)
    dictOfTopDicts[airline] = list(zip(top.index, top.values))

print(dictOfTopDicts)

for airline in pathsManager.LIST_OF_AIRLINES:
    print(airline)
    print(', '.join([word +':'+str(count) for word, count in dictOfTopDicts[airline][0:14]]))
    print('------')


#Potential stop words - create list of joined top words list
#If one word appears in all of airlines, then it is potential stop word
allTopWordsList = []
for airline in pathsManager.LIST_OF_AIRLINES:
    topWordsList = [key_word for (key_word, count) in dictOfTopDicts[airline]]
    for word in topWordsList:
        allTopWordsList.append(word)

#Use counter to calculate frequency of top word
topWordsAmongAirlines = Counter(allTopWordsList).most_common()
print("########")
print(topWordsAmongAirlines)
print("########")
print("## potential stop words ##")
potentialStopWords = []
for word, count in topWordsAmongAirlines:
    if count == 3:
        potentialStopWords.append(word)
print(potentialStopWords)
print("########")


stopWordsListFromShortWords = stopWordsManager.createStopWordsListFromShortWords(lemmatizedDataDictForCorpusWithoutStopWords, 3)

CUSTOM_STOP_WORDS = ['didnt', 'werent', 'dont', 'doesnt', 'wasnt', 'isnt', 'arent', 'havent', 'hasnt', 'hadnt']

#Order is important here, because text.ENGLISH_STOP_WORDS is the frozenset
UNION_STOP_WORDS = stopWordsListFromShortWords\
    .union(stopWordsListFromShortWords)\
    .union(countVectorizer.get_stop_words())
    # .union(potentialStopWords)
objectManager.saveObject(UNION_STOP_WORDS, pathsManager.UNION_STOP_WORDS)

print(UNION_STOP_WORDS)
