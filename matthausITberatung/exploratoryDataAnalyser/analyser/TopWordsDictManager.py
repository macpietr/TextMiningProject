class TopWordsDictManager:

    def getTopCommonWords(self, dataDictOfCountedWords, numberOfTopWordsPerAirline):
        topCommonWords = []
        for airline in dataDictOfCountedWords:
            topWordsPerAirline = [word for (word, count) in dataDictOfCountedWords[airline].most_common(numberOfTopWordsPerAirline)]
            for topWord in topWordsPerAirline:
                topCommonWords.append(topWord)
        return topCommonWords;

    def printTopWords(self, dataDictOfCountedWords, numberOfWordsToPrint):
        for key in dataDictOfCountedWords:
            print(key)
            print('; '.join([word + ':' + str(count) for word, count in dataDictOfCountedWords[key].most_common(numberOfWordsToPrint)]))
            print('-----')
