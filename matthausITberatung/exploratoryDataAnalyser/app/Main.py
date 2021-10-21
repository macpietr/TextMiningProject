from collections import Counter

from matplotlib import pyplot as plt
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud

from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.exploratoryDataAnalyser.analyser.TopWordsDictManager import TopWordsDictManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.stopWords.manager.StopWordsManager import StopWordsManager


##BASIC PART
#Create objects which are managers for certain operations
corpusManager = CorpusManager()
dataTermMatrixManager = DataTermMatrixManager()
objectManager = ObjectsManager()
topWordsDictManager = TopWordsDictManager()
stopWordsManager = StopWordsManager()

POTENTIAL_STOP_WORDS_LIST = objectManager.getSavedObject('potentialStopWordsList')
UNION_STOP_WORDS = text.ENGLISH_STOP_WORDS.union(POTENTIAL_STOP_WORDS_LIST)
#CountVectorizer will be required object to create DTM
#It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text.
countVectorizer = CountVectorizer(stop_words=UNION_STOP_WORDS)

#We have to create corpus
mainOpinionsCorpus = corpusManager.createMainOpinionsCorpus()

print(mainOpinionsCorpus)

#name columns with opinions from corpus as 'opinions'. We have only one column in our corpus, beacuse airlines are index of corpus
mainOpinionsCorpus.columns = ['opinions']

#Create DTM basing on previous corpus and countVectorizer which takes stop words into account
mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions, countVectorizer)

#assign corpus index to DTM index. It replaces numeric index with appropriate airline names brought from corpus
#rows of DTM are labeled as certain arilines.
mainOpinionsDTM.index = mainOpinionsCorpus.index

#print(mainOpinionsDTM.columns)

print(mainOpinionsDTM.transpose().head(30))

#Create a dictionary where key is the airline and value is a list of words and their number of appearance (word, count)
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


#########PLOTS

airlines = topWordsDict.keys()

projectWordcloud = WordCloud(stopwords=UNION_STOP_WORDS, background_color="white", colormap="Dark2", max_font_size=150, random_state=42)

plt.rcParams['figure.figsize'] = [50,50]

projectWordcloud.generate(mainOpinionsCorpus.opinions['lufthansa'])
plt.subplot(4,4,1)
plt.imshow(projectWordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("heheheh")

plt.show()