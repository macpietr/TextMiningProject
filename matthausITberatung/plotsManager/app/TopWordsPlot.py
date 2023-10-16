import matplotlib.pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

pathsManager = PathsManager()
objectsManager = ObjectsManager()

dictOfListOf30CountedMostCommonWords = objectsManager.getSavedObject(pathsManager.DICT_OF_LIST_OF_30_COUNTED_MOST_COMMON_WORDS)
dictOfListOf30CountedMostCommonBigrams = objectsManager.getSavedObject(pathsManager.DICT_OF_LIST_OF_30_COUNTED_MOST_COMMON_BIGRAMS)


for airline in pathsManager.LIST_OF_AIRLINES:
        topWordsList = dictOfListOf30CountedMostCommonWords[airline]
        topWordsDict = dict(topWordsList)
        print(len(topWordsDict))
        plt.figure(figsize=(15,8))
        plt.bar(range(len(topWordsDict)),
                list(topWordsDict.values()),
                tick_label=list(topWordsDict.keys()),
                align='center', width=0.6)
        plt.xticks(rotation=55)
        plt.title(airline, fontsize=20)
        plt.show()