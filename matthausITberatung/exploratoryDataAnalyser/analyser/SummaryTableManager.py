import pandas


class SummaryTableManager:


    def createSummaryTable(self, dataTermMatrix):
        summaryTable = pandas.DataFrame(dataTermMatrix.columns, columns=['airlines'])
        summaryTable['unique_words'] = self.__getCountOfUniqueWordsList(dataTermMatrix)
        summaryTable['sum_of_words'] = self.__getTotalNumberOfWords(dataTermMatrix)
        summaryTable['sum_of_words_per_post'] = summaryTable['sum_of_words'] / 1000
        return summaryTable

    def __getTotalNumberOfWords(self, dataTermMatrix):
        totalNumberOfWordsList = []
        for airline in dataTermMatrix.columns:
            totalNumberOfWords = sum(dataTermMatrix[airline])
            totalNumberOfWordsList.append(totalNumberOfWords)
        return totalNumberOfWordsList

    def __getCountOfUniqueWordsList(self, dataTermMatrix):
        countOfUniqueWordsList = []
        for airline in dataTermMatrix.columns:
            uniqueWord = dataTermMatrix[airline].to_numpy().nonzero()[0].size
            countOfUniqueWordsList.append(uniqueWord)
        return countOfUniqueWordsList



