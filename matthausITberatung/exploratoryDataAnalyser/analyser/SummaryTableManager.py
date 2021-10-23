import pandas


class UniqueWordsManager:

    def createUniqueWordsTable(self, dataTermMatrix):
        return pandas.DataFrame(list(zip(dataTermMatrix.columns,
                self.__getCountOfUniqueWordsList(dataTermMatrix))),
                columns=['airlines', 'unique_words'])

    def __getCountOfUniqueWordsList(self, dataTermMatrix):
        countOfUniqueWordsList = []
        for airline in dataTermMatrix.columns:
            uniqueWord = dataTermMatrix[airline].to_numpy().nonzero()[0].size
            countOfUniqueWordsList.append(uniqueWord)
        return countOfUniqueWordsList
