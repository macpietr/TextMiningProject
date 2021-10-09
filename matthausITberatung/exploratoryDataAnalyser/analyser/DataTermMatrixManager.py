import pandas
from sklearn.feature_extraction.text import CountVectorizer


class DataTermMatrixManager:

    def __init__(self):
        self.countVectoriser = CountVectorizer(stop_words='english')

    def createDataTermMatrix(self, corpusColumn):
        return pandas.DataFrame(self.getCountedWordsArray(corpusColumn), columns=self.getCountedWordsLabels())

    def getCountedWordsLabels(self):
        return self.countVectoriser.get_feature_names_out()

    def getCountedWordsArray(self, corpusColumn):
        return self.getCountedWordsVector(corpusColumn).toarray()

    def getCountedWordsVector(self, corpusColumn):
        return self.countVectoriser.fit_transform(corpusColumn)

