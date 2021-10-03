import pandas
import pickle
from pandas import DataFrame

from matthausITberatung.exploratoryDataAnalyser.analyser.corpus.CleanedDataDict import CleanedDataDict
from matthausITberatung.fileManager.PathsManager import PathsManager


class CorpusManager:

    def createCorpus(self, *numberOfCharactersToPrint):
        cleanDataDictForCorpus = CleanedDataDict().getCleanedDataDictForCorpus()
        if len(numberOfCharactersToPrint) == 0:
            return DataFrame.from_dict(cleanDataDictForCorpus).transpose()
        if len(numberOfCharactersToPrint) == 1:
            pandas.set_option('max_colwidth',numberOfCharactersToPrint[0])
            return DataFrame.from_dict(cleanDataDictForCorpus).transpose()
        elif len(numberOfCharactersToPrint) > 1:
            print('Maximum number of parameters is 1 for getCorpus() method')

    def saveCorpus(self, corpusObject, objectfileName):
        corpusObject.to_pickle(PathsManager().PICKLED_FILES()+'/'+objectfileName+'.pkl')

    def getSavedCorpus(self, objectFileName):
        return pandas.read_pickle(PathsManager().PICKLED_FILES()+'/'+objectFileName+'.pkl')
