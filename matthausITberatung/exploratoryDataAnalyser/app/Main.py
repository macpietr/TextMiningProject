
from matthausITberatung.exploratoryDataAnalyser.analyser.corpus.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.dataTermMatrix.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

corpusManager = CorpusManager()
dataTermMatrixManager = DataTermMatrixManager()
objectManager = ObjectsManager()

mainOpinionsCorpus = corpusManager.createMainOpinionsCorpus()
mainOpinionsCorpus.columns = ['opinions']

mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions)
objectManager.saveObject(mainOpinionsDTM, 'mainOpinionsDTM')
print(objectManager.getSavedObject('mainOpinionsDTM'))


# mainOpinionsDTM = dataTermMatrixManager.createDataTermMatrix(mainOpinionsCorpus.opinions)
#
# print(mainOpinionsDTM)


# data_cv = countVectorizer.fit_transform(corpus.opinions)
# print(data_cv)
# print('#############')
# data_dtm = pandas.DataFrame(data_cv.toarray(), columns=countVectorizer.get_feature_names_out())
# print('#############')
# print(data_cv.toarray())
# print(countVectorizer.get_feature_names_out())
# print('#############')
# print(data_dtm)


# corpusManager = CorpusManager()
#
# generalCorpus = corpusManager.createCorpus(150)
# generalCorpus.columns = ['opinions']
#
# print(generalCorpus.items)
