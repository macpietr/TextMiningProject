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

# lufthansaListOfMainOpinionsPolarity = []
# for line in lufthansaListOfMainOpinions:
#     lufthansaListOfMainOpinionsPolarity.append(TextBlob(line).sentiment.polarity)

lufthansaZippedList = list(zip(lufthansaListOfDateFlown,lufthansaListOfMainOpinions))

lufthansaZippedListOfDateFlownAndOpinion2021 = []
for dateFlownAndOpinion in lufthansaZippedList:
    if dateFlownAndOpinion[0][len(dateFlownAndOpinion) - 6:] == '2021':
        lufthansaZippedListOfDateFlownAndOpinion2021.append(dateFlownAndOpinion)

print(lufthansaZippedListOfDateFlownAndOpinion2021)

lufthansaListOfDateFlown2021, lufthansaListOfMainOpinions2021 = zip(*lufthansaZippedListOfDateFlownAndOpinion2021)

print(lufthansaListOfDateFlown2021)

lufthansaDateFlown2021Counter = Counter(lufthansaListOfDateFlown2021)

print(lufthansaDateFlown2021Counter)
print(lufthansaDateFlown2021Counter.keys())

dataDictOfDateFlownAndCollectedOpinions2021 = {}
for dateFlown in lufthansaDateFlown2021Counter.keys():
    listOfOpinionsForCertainDate = []
    for dateFlownAndOpinion in lufthansaZippedListOfDateFlownAndOpinion2021:
        if str(dateFlownAndOpinion[0]) == str(dateFlown):
            listOfOpinionsForCertainDate.append(dateFlownAndOpinion[1])
    dataDictOfDateFlownAndCollectedOpinions2021[dateFlown] = ' '.join(listOfOpinionsForCertainDate)
#     print('')
#
# for item in dataDictOfDateFlownAndCollectedOpinions2021.items():
#     print(item)

dataDictOfDateFlownAndCollectedOpinions2021Polarity = {}
for dateFlown in dataDictOfDateFlownAndCollectedOpinions2021.keys():
    dataDictOfDateFlownAndCollectedOpinions2021Polarity[dateFlown] = \
        TextBlob(dataDictOfDateFlownAndCollectedOpinions2021[dateFlown]).sentiment.polarity

[print(item) for item in dataDictOfDateFlownAndCollectedOpinions2021Polarity.items()]

# dictOfDateFlownAndAvgPolarity = {}
# for dateFlown in lufthansaDateFlown2021Counter.keys():
#     listToSum = []
#     for dateFlownAndOpinion in lufthansaZippedListOfDateFlownAndOpinion2021:
#         if str(dateFlownAndOpinion[0]) == str(dateFlown):
#             listToSum.append(dateFlownAndOpinion[1])
#     dictOfDateFlownAndAvgPolarity[dateFlown] = sum(listToSum) / lufthansaDateFlown2021Counter[dateFlown]

# print(dictOfDateFlownAndAvgPolarity)
#
# plt.plot(dictOfDateFlownAndAvgPolarity.keys(),dictOfDateFlownAndAvgPolarity.values())
# plt.show()

plt.plot(dataDictOfDateFlownAndCollectedOpinions2021Polarity.keys(),dataDictOfDateFlownAndCollectedOpinions2021Polarity.values())
plt.show()

# print(lufthansaZippedList[0][0][len(lufthansaZippedList[0][0])-4:])

# TODO: check what will happen if we would count poalrity from post created form 17 posts insted of average polarity
# TODO: the outcomes of polarity of concatenated ofinions differs from average polarity of separate opinions. Which measure is more relevant?