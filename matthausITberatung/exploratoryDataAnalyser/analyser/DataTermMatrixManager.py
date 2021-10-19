import pandas

class DataTermMatrixManager:

    def createDataTermMatrix(self, corpusColumn, countVectorizer):
        # make a DTM where columns are labeled as words appeared in opinions about airlines
        # Values of matrix show quantity of word in opinions for certain airline
        return pandas.DataFrame(self.__getCountedWordsArray(corpusColumn, countVectorizer),
                                columns=self.__getCountedWordsLabels(countVectorizer))

    #Below methods are private, beacuse they have to be invoked in appropriate order. It is not allowed to return
    #CountedWirdsLabels without previous usage of fit_transform on countVectoriser
    def __getCountedWordsLabels(self, countVectorizer):
        return countVectorizer.get_feature_names_out()

    def __getCountedWordsArray(self, corpusColumn, countVectorizer):
        return self.__getCountedWordsVector(corpusColumn, countVectorizer).toarray()

    def __getCountedWordsVector(self, corpusColumn, countVectorizer):
        return countVectorizer.fit_transform(corpusColumn)

