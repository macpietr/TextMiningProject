from collections import Counter

from sklearn.feature_extraction.text import CountVectorizer

from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.exploratoryDataAnalyser.analyser.TopWordsDictManager import TopWordsDictManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.stopWords.StopWordsManager import StopWordsManager

corpusManager = CorpusManager()
dataTermMatrixManager = DataTermMatrixManager()
objectManager = ObjectsManager()
topWordsDictManager = TopWordsDictManager()
stopWordsManager = StopWordsManager()

mainOpinionsCorpus = corpusManager.createMainOpinionsCorpus()
#print(mainOpinionsCorpus)
#print("####################")
#name columns with opinions from corpus as 'opinions'. We have only one column in our corpus, beacuse airlines are index of corpus
mainOpinionsCorpus.columns = ['opinions']
#print(mainOpinionsCorpus)
#print("####################")
countVectorizer = CountVectorizer(stop_words='english')
mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions, countVectorizer)
#print(mainOpinionsDTM)
#assign corpus index to DTM index. It replaces numeric index with appropriate airline names brought from corpus
#rows of DTM are labeled as certain arilines.
mainOpinionsDTM.index = mainOpinionsCorpus.index
#print(mainOpinionsDTM)
#print(mainOpinionsDTM.transpose())

#print(mainOpinionsDTM.columns)

print(mainOpinionsDTM.transpose().head(30))

topWordsDict = topWordsDictManager.createTopWordsDict(mainOpinionsDTM.transpose())

#print(topWordsDict)

topWordsDictManager.printTopWords(topWordsDict,12)

print(topWordsDict["lufthansa"][0:14])



#Poniżej wrzucamy 30 najczęściej występujących słów do tablicy words dla każdej lini lotniczej

topCommonWords = topWordsDictManager.getTopCommonWords(topWordsDict,30)

print(len(topWordsDictManager.getTopCommonWords(topWordsDict,30)))
#Dzięki counterowi, możemy wskazać, które słowo z wcześniej wrzuconych powtórzuło się. Otzymujemy słowo i numer w ilu opiniach lini lotniczych wystąpiło
print(type(Counter(topCommonWords).most_common()))
#Możemy zdecydować, które spośród tych słów trafi do stop words, a które będziemy badać
print(len(topWordsDict.keys()))
potentialStopWordsList = stopWordsManager.createPotentialStopWordsList(topCommonWords,3)
print(potentialStopWordsList)