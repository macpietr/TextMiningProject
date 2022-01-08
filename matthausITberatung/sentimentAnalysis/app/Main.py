from collections import Counter

from matplotlib import pyplot as plt
from textblob import TextBlob

from matthausITberatung.objectsManager.CollectionsFromFiles import CollectionsFromFiles

collectionsFromFiles = CollectionsFromFiles()
airlinesDictOfListsOfMainOpinions = collectionsFromFiles.createDictOfListsOfRecordsFromDownloadedFile('MainUserOpinion')
airlinesDictOfListsOfDateFlown = collectionsFromFiles.createDictOfListsOfRecordsFromDownloadedFile('DateFlown')

lufthansaListOfMainOpinions = airlinesDictOfListsOfMainOpinions['lufthansa']
del lufthansaListOfMainOpinions[len(lufthansaListOfMainOpinions)-1]
lufthansaListOfDateFlown = airlinesDictOfListsOfDateFlown['lufthansa']
del lufthansaListOfDateFlown[len(lufthansaListOfDateFlown) - 1]

lufthansaListOfMainOpinionsPolarity = []
for line in lufthansaListOfMainOpinions:
    lufthansaListOfMainOpinionsPolarity.append(TextBlob(line).sentiment.polarity)

lufthansaZippedList = list(zip(lufthansaListOfDateFlown,lufthansaListOfMainOpinionsPolarity))

lufthansaZippedList2021 = []
for line in lufthansaZippedList:
    if line[0][len(line)-6:] == '2021':
        lufthansaZippedList2021.append(line)

print(lufthansaZippedList2021)

lufthansaListOfDateFlown2021, lufthansaListOfMainOpinionsPolarity2021 = zip(*lufthansaZippedList2021)

print(lufthansaListOfDateFlown2021)

lufthansaDateFlown2021Counter = Counter(lufthansaListOfDateFlown2021)

print(lufthansaDateFlown2021Counter)
print(lufthansaDateFlown2021Counter.keys())

dictOfDateFlownAndAvgPolarity = {}
for key in lufthansaDateFlown2021Counter.keys():
    listToSum = []
    for line in lufthansaZippedList2021:
        if str(line[0]) == str(key):
            listToSum.append(line[1])
    dictOfDateFlownAndAvgPolarity[key] = sum(listToSum)/lufthansaDateFlown2021Counter[key]

print(dictOfDateFlownAndAvgPolarity)

plt.plot(dictOfDateFlownAndAvgPolarity.keys(),dictOfDateFlownAndAvgPolarity.values())
plt.show()

# print(lufthansaZippedList[0][0][len(lufthansaZippedList[0][0])-4:])

# TODO: check what will happen if we would count poalrity from post created form 17 posts insted of average polarity