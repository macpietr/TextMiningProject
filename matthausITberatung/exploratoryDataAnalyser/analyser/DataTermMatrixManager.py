import pandas
from sklearn.feature_extraction.text import CountVectorizer


class DataTermMatrixManager:

    def __init__(self):
        self.countVectoriser = CountVectorizer(stop_words='english')

    def createDataTermMatrix(self, corpusColumn):
        return pandas.DataFrame(self.__getCountedWordsArray(corpusColumn), columns=self.__getCountedWordsLabels())

    def __getCountedWordsLabels(self):
        return self.countVectoriser.get_feature_names_out()

    def __getCountedWordsArray(self, corpusColumn):
        return self.__getCountedWordsVector(corpusColumn).toarray()

    def __getCountedWordsVector(self, corpusColumn):
        return self.countVectoriser.fit_transform(corpusColumn)

