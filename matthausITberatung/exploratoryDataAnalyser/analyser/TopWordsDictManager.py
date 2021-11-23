class TopWordsDictManager:

    #Make a dict where key is the airline and value is array of words and the number of theirs appearances
    def createTopWordsDict(self, TermDataMatrix):
        topWordsDict = {}
        for column in TermDataMatrix.columns:
            #sort numbers of certain word appearance descending
            top = TermDataMatrix[column].sort_values(ascending=False)
            #zip index of those numbers with them. Thus we obtain array of pairs - (word, number of appearances)
            #TODO: zastanowić się czy nie zrobić dla poniższej linijki wariantu z dictem, tak aby móc wyciągać sobie konkretny wyraz i ilość wystąpień dla niego
            topWordsDict[column] = list(zip(top.index, top.values))
        return topWordsDict

    def getTopCommonWords(self, topWordsDict, numberOfTopWordsPerAirline):
        topCommonWords = []
        for airline in topWordsDict:
            topWordsPerAirline = [word for (word, count) in topWordsDict[airline][0:numberOfTopWordsPerAirline]]
            for topWord in topWordsPerAirline:
                topCommonWords.append(topWord)
        return topCommonWords;

    def printTopWords(self, topWordsDict, numberOfWordsToPrint):
        for key in topWordsDict:
            print(key)
            print('; '.join([word + ':' + str(count) for word, count in topWordsDict[key][0:numberOfWordsToPrint]]))
            print('-----')
