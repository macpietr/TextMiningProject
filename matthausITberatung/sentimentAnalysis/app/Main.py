from matthausITberatung.objectsManager.CollectionsFromFiles import CollectionsFromFiles

collectionsFromFiles = CollectionsFromFiles()
airlinesDictOfListsOfMainOpinions = collectionsFromFiles.createDictOfListsOfRecordsFromDownloadedFile('MainUserOpinion')
airlinesDictOfListsOfDateFlown = collectionsFromFiles.createDictOfListsOfRecordsFromDownloadedFile('DateFlown')

airlinesDictOfZippedLists = {}
for key in airlinesDictOfListsOfMainOpinions.keys():
    airlinesDictOfZippedLists[key] = list(zip(airlinesDictOfListsOfDateFlown[key],airlinesDictOfListsOfMainOpinions[key]))

print(airlinesDictOfZippedLists['lufthansa'][998])

#TODO: use DateFlown and MainOpinions to sentiment analysis plots in time. Use DateFlown as time and opinions as positive or negative indicator of sentiment analysis