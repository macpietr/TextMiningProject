import pandas
from pandas import DataFrame

from matthausITberatung.exploratoryDataAnalyser.analyser.corpus.CleanedDataDict import CleanedDataDict

class Corpus:

    def getCorpus(self, *numberOfCharactersToPrint):
        cleanDataDictForCorpus = CleanedDataDict().getCleanedDataDictForCorpus()
        if len(numberOfCharactersToPrint) == 0:
            return DataFrame.from_dict(cleanDataDictForCorpus).transpose()
        if len(numberOfCharactersToPrint) == 1:
            pandas.set_option('max_colwidth',numberOfCharactersToPrint[0])
            return DataFrame.from_dict(cleanDataDictForCorpus).transpose()
        elif len(numberOfCharactersToPrint) > 1:
            print('Maximum number of parameters is 1 for getCorpus() method')