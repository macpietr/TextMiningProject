import matplotlib.pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

pathsManager = PathsManager()
objectManager = ObjectsManager()

airlinesDictOfCountedWordsCounter = ObjectsManager().getSavedObject(pathsManager.AIRLINES_DICT_OF_COUNTED_WORDS_COUNTER)

lufthansaTopWordsList = airlinesDictOfCountedWordsCounter['lufthansa'].most_common(20)

lufthansaTopWordsDict = dict(lufthansaTopWordsList)



print(len(lufthansaTopWordsDict))

plt.figure(figsize=(10,6))
plt.bar(range(len(lufthansaTopWordsDict)),
        list(lufthansaTopWordsDict.values()),
        tick_label=list(lufthansaTopWordsDict.keys()),
        align='center', width=0.6)
plt.xticks(rotation=35)
plt.show()