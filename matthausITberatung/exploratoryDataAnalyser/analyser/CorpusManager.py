import pandas
from pandas import DataFrame

class CorpusManager:

    def createCorpus(self, dataDictForCorpus, numberOfCharactersToPrint):
        pandas.set_option('max_colwidth', numberOfCharactersToPrint)
        return DataFrame(dataDictForCorpus, index=[0]).transpose()
