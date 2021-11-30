import pandas
from pandas import DataFrame

from matthausITberatung.exploratoryDataAnalyser.analyser.CleanedDataDictManager import CleanedDataDictManager
from matthausITberatung.objectsManager.PathsManager import PathsManager


class CorpusManager:

    def createCorpus(self, dataDictForCorpus, numberOfCharactersToPrint):
        pandas.set_option('max_colwidth', numberOfCharactersToPrint)
        return DataFrame.from_dict(dataDictForCorpus).transpose()

    def saveCorpus(self, corpusObject, objectfileName):
        corpusObject.to_pickle(PathsManager().PICKLED_FILES+'/'+objectfileName+'.pkl')

    def getSavedCorpus(self, objectFileName):
        return pandas.read_pickle(PathsManager().PICKLED_FILES+'/'+objectFileName+'.pkl')
