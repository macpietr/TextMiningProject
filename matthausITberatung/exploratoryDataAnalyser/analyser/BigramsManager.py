from nltk import ngrams

from matthausITberatung.exploratoryDataAnalyser.analyser.CleanedDataDictManager import CleanedDataDictManager
from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.exploratoryDataAnalyser.analyser.SummaryTableManager import SummaryTableManager
from matthausITberatung.exploratoryDataAnalyser.analyser.TopWordsDictManager import TopWordsDictManager
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

bigramsCorpus = CorpusManager().createCorpus(dictForCorpus, 30)
bigramsCorpus.columns = ['bigramOpinions']
bigramsDTM = DataTermMatrixManager().createDataTermMatrix(bigramsCorpus.bigramOpinions, countVectorizer)
bigramsDTM.index = bigramsCorpus.index

print(bigramsCorpus)
print("########")

bigramsTDM = bigramsDTM.transpose()

bigramsTopWordsDict = TopWordsDictManager().createTopWordsDict(bigramsTDM)

TopWordsDictManager().printTopWords(bigramsTopWordsDict,12)

topCommonBigramsWords = TopWordsDictManager().getTopCommonWords(bigramsTopWordsDict,30)

print(topCommonBigramsWords)

bigramsSummaryTable = SummaryTableManager().createSummaryTable(bigramsTDM)

print('##### bigrams summary table #####')
print(bigramsSummaryTable)