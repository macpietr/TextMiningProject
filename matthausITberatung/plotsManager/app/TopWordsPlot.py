import matplotlib.pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

pathsManager = PathsManager()
objectsManager = ObjectsManager()

dictOfListOf30CountedMostCommonWords = objectsManager.getSavedObject(pathsManager.DICT_OF_LIST_OF_30_COUNTED_MOST_COMMON_WORDS)
dictOfListOf30CountedMostCommonBigrams = objectsManager.getSavedObject(pathsManager.DICT_OF_LIST_OF_30_COUNTED_MOST_COMMON_BIGRAMS)

lufthansaTopWordsList = dictOfListOf30CountedMostCommonBigrams['lufthansa']

lufthansaTopWordsDict = dict(lufthansaTopWordsList)



print(len(lufthansaTopWordsDict))

plt.figure(figsize=(15,8))
plt.bar(range(len(lufthansaTopWordsDict)),
        list(lufthansaTopWordsDict.values()),
        tick_label=list(lufthansaTopWordsDict.keys()),
        align='center', width=0.6)
plt.xticks(rotation=55)
plt.show()