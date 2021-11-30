from nltk import ngrams

from matthausITberatung.exploratoryDataAnalyser.analyser.CleanedDataDictManager import CleanedDataDictManager
from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

mainOpinionsCorpus = ObjectsManager().getSavedObject('mainOpinionsCorpus')
countVectorizer = ObjectsManager().getSavedObject('countVectorizer')

dictOfBigrams = {}
for airline in PathsManager().LIST_OF_AIRLINES:
    dictOfBigrams[airline] = ngrams(mainOpinionsCorpus.opinions[airline].split(), 2)

dataDict = {}
for airline in PathsManager().LIST_OF_AIRLINES:
    listOfBigrams = [' '.join(bigram) for bigram in dictOfBigrams[airline]]
    fullString = ' '.join(listOfBigrams)
    dataDict[airline] = fullString

dictForCorpus = CleanedDataDictManager().getDataDictForCorpus(dataDict)

corpus = CorpusManager().createCorpus(dictForCorpus, 30)
corpus.columns = ['bigramOpinions']
DTM = DataTermMatrixManager().createDataTermMatrix(corpus.bigramOpinions, countVectorizer)
DTM.index = corpus.index

print(corpus)
print("########")
print(DTM)

# dictOfStringFromBigrams = {}
# for airline in PathsManager().LIST_OF_AIRLINES:
#     stringFromBigram = ""
#     for (item1, item2) in dictOfBigrams[airline]:
#         stringFromBigram = " "+item1+" "+item2
#     dictOfStringFromBigrams[airline] = stringFromBigram

# print(dictOfStringFromBigrams['lufthansa'][0:14])


#jeszcze bigrams obrobic na jednolity string dla kazdej lini lotniczej
#z tych stringow zbudowac dict
#z tego dicta zbudowac corpus
#z tego corpusu zbudowac DTM uwzgledniaja countVectorizer z wbudowanymi końcowymi stop_wordsami
#z tego DTMa zbudowac wordcloud

#
# for item in bigram:
#     print(item)
#
# sentence = 'this is a foo bar sentences and i want to ngramize it'
#
# n = 6
# sixgrams = ngrams(sentence.split(), n)
#
# for grams in sixgrams:
#   print(grams)

#
# dataDict = {}
# for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES):
#     dataDict[airline] = ngrams(mainOpinionsCorpus.opinions[airline].split(), 2)
#
# print(dataDict['lufthansa'])

# bigramCorpus = CorpusManager().createCorpus(dataDict, 30)
# bigramCorpus.columns = ['bigram_opinions']
#
# DTM = DataTermMatrixManager().createDataTermMatrix(bigramCorpus.bigram_opinions, countVectorizer)