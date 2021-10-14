from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.exploratoryDataAnalyser.analyser.TopWordsDictManager import TopWordsDictManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

corpusManager = CorpusManager()
dataTermMatrixManager = DataTermMatrixManager()
objectManager = ObjectsManager()
topWordsDictManager = TopWordsDictManager()

mainOpinionsCorpus = corpusManager.createMainOpinionsCorpus()
print(mainOpinionsCorpus)
print("####################")
#name columns with opinions from corpus as 'opinions'. We have only one column in our corpus, beacuse airlines are index of corpus
mainOpinionsCorpus.columns = ['opinions']
print(mainOpinionsCorpus)
print("####################")

mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions)
print(mainOpinionsDTM)
#assign corpus index to DTM index. It replaces numeric index with appropriate airline names brought from corpus
mainOpinionsDTM.index = mainOpinionsCorpus.index
print(mainOpinionsDTM)
print(mainOpinionsDTM.transpose())

print(mainOpinionsDTM.columns)

topWordsDict = topWordsDictManager.createTopWordsDict(mainOpinionsDTM.transpose())

print(topWordsDict)

topWordsDictManager.printTopWords(topWordsDict,4)

