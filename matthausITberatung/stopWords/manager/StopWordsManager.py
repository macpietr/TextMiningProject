from collections import Counter


class StopWordsManager:

    def createStopWordsListBasedOnCommonWords(self, topCommonWords, numberOfDocumentsInWhichWordsOccured):
        potentialStopWordsList = [word for (word, count) in Counter(topCommonWords).most_common() if count >= numberOfDocumentsInWhichWordsOccured]
        return potentialStopWordsList

    def createStopWordsListFromShortWords(self, dataDict, maxLengthOfWords):
        wholeString = ''
        for key in dataDict.keys():
            wholeString=wholeString+str(dataDict[key])
        return set([''.join(word.strip()) for word in wholeString.split(' ') if len(word.strip()) <= maxLengthOfWords])