import os


class FileWriter:

    def __init__(self, airLineName, filenameSuffix, parentDirectoryName):
        self.filename = airLineName + '_' + filenameSuffix
        self.childDirectoryName = filenameSuffix
        self.parentDirectoryName = parentDirectoryName

    def OUTPUT_DIRECTORY(self):
        path = self.parentDirectoryName
        if not (os.path.exists(path)):
            os.mkdir(path)
        path = path + '\\' + self.childDirectoryName
        if not (os.path.exists(path)):
            os.mkdir(path)
        return path+'\\'

    def putExtractedDataIntoFile(self, arrayOfArraysData):
        with open(str(self.OUTPUT_DIRECTORY() + self.filename) + '.txt', 'w', encoding='utf-8') as outfile:
            for dataArray in arrayOfArraysData:
                for dataItem in dataArray:
                    print(dataItem, file=outfile)
