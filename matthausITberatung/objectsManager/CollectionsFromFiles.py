from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.PathsManager import PathsManager


class CollectionsFromFiles:

    def __init__(self):
        self.pathsManager = PathsManager()
        self.fileReader = FileReader()

    def createDictOfListsOfRecordsFromDownloadedFile(self, childDir):
        dictOfListsOfRecordsFromDownloadedFile = {}
        for airline in self.pathsManager.LIST_OF_AIRLINES:
            dictOfListsOfRecordsFromDownloadedFile[airline] = self.fileReader \
                .readFile(PathsManager().DOWNLOADED_FILES_DIR, childDir, airline) \
                .split('\n')
        if dictOfListsOfRecordsFromDownloadedFile[airline][len(dictOfListsOfRecordsFromDownloadedFile[airline]) - 1] == '':
            del dictOfListsOfRecordsFromDownloadedFile[airline][len(dictOfListsOfRecordsFromDownloadedFile[airline]) - 1]
        return dictOfListsOfRecordsFromDownloadedFile