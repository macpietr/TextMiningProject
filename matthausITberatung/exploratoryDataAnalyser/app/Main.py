from matthausITberatung.exploratoryDataAnalyser.analyser.corpus.CleanedDataDict import CleanedDataDict
from matthausITberatung.exploratoryDataAnalyser.analyser.corpus.Corpus import Corpus
from matthausITberatung.fileManager.PathsManager import PathsManager

cdd = CleanedDataDict()


print(cdd.getCleanedDataDict().keys())
corpus = Corpus().getCorpus(150)
corpus.columns = ['opinions']
print(corpus)

corpus = corpus.sort_index()

print(corpus)