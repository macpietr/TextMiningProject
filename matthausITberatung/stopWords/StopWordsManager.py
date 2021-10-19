from collections import Counter


class StopWordsManager:

    def createPotentialStopWordsList(self, topCommonWords, numberOfDocumentsInWhichWordsOccured):
        potentialStopWordsList = [word for (word, count) in Counter(topCommonWords).most_common() if count >= numberOfDocumentsInWhichWordsOccured]
        return potentialStopWordsList