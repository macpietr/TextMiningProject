import matplotlib.pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

topWordsDict = ObjectsManager().getSavedObject("topWordsDict")

lufthansaTopWordsList = topWordsDict['lufthansa'][0:20]

lufthansaTopWordsDict = dict(lufthansaTopWordsList)

print(len(lufthansaTopWordsDict))

plt.figure(figsize=(10,6))
plt.bar(range(len(lufthansaTopWordsDict)),
        list(lufthansaTopWordsDict.values()),
        tick_label=list(lufthansaTopWordsDict.keys()),
        align='center', width=0.6)
plt.xticks(rotation=35)
plt.show()