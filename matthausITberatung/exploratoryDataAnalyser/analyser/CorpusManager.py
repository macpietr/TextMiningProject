import pandas
from pandas import DataFrame

from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager
from matthausITberatung.objectsManager.PathsManager import PathsManager


class CorpusManager:

    ##TODO: remove stop_words from corpus instead of DTM, thanks to this, creation of appropriate bigrams list will be easier
    def createCorpus(self, dataDictForCorpus, numberOfCharactersToPrint):
        pandas.set_option('max_colwidth', numberOfCharactersToPrint)
        return DataFrame(dataDictForCorpus, index=[0]).transpose()

    def saveCorpus(self, corpusObject, objectfileName):
        corpusObject.to_pickle(PathsManager().PICKLED_FILES+'/'+objectfileName+'.pkl')

    def getSavedCorpus(self, objectFileName):
        return pandas.read_pickle(PathsManager().PICKLED_FILES+'/'+objectFileName+'.pkl')
