class TopWordsDictManager:

    #Make a dict where key is the airline and value is array of words and the number of theirs appearances
    def createTopWordsDict(self, DataTermMatrix):
        topWorldsDict = {}
        for column in DataTermMatrix.columns:
            #sort numbers of certain word appearance descending
            top = DataTermMatrix[column].sort_values(ascending=False)
            #zip index of those numbers with them. Thus we obtain array of pairs - (word, number of appearances)
            topWorldsDict[column] = list(zip(top.index, top.values))
        return topWorldsDict

    def printTopWords(self, topWordsDict, numberOfWordsToPrint):
        for key in topWordsDict:
            print(key)
            print('; '.join([word + ':' + str(count) for word, count in topWordsDict[key][0:numberOfWordsToPrint]]))
            print('-----')
