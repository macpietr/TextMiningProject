class TopWordsDictManager:

    def createTopWordsDict(self, DataTermMatrix):
        topWorldsDict = {}
        for column in DataTermMatrix.columns:
            top = DataTermMatrix[column].sort_values(ascending=False)
            topWorldsDict[column] = list(zip(top.index, top.values))
        return topWorldsDict

    def printTopWords(self, topWordsDict, numberOfWordsToPrint):
        for key in topWordsDict:
            print(key)
            print('; '.join([word + ':' + str(count) for word, count in topWordsDict[key][0:numberOfWordsToPrint]]))
            print('-----')
