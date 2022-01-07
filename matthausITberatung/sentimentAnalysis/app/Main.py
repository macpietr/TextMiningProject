from matthausITberatung.objectsManager.CollectionsFromFiles import CollectionsFromFiles

collectionsFromFiles = CollectionsFromFiles()
airlinesDictOfListsOfMainOpinions = collectionsFromFiles.createDictOfListsOfRecordsFromDownloadedFile('MainUserOpinion')
airlinesDictOfListsOfDateFlown = collectionsFromFiles.createDictOfListsOfRecordsFromDownloadedFile('DateFlown')

airlinesDictOfZippedLists = {}
for key in airlinesDictOfListsOfMainOpinions.keys():
    airlinesDictOfZippedLists[key] = list(zip(airlinesDictOfListsOfDateFlown[key],airlinesDictOfListsOfMainOpinions[key]))

print(airlinesDictOfZippedLists['lufthansa'][998])
