import os


class FileWriter:

    def __init__(self, airLineName, arrayOfArraysData, filenameSuffix, parentDirectoryName):
        self.arrayOfArraysData = arrayOfArraysData
        self.childDirectoryName = filenameSuffix
        self.filename = airLineName + '_' + filenameSuffix
        self.parentDirectoryName = parentDirectoryName

    def OUTPUT_DIRECTORY(self):
        path = self.parentDirectoryName
        if not (os.path.exists(path)):
            os.mkdir(path)
        path = path + '\\' + self.childDirectoryName
        if not (os.path.exists(path)):
            os.mkdir(path)
        return path+'\\'

    def putExtractedDataIntoFile(self):
        with open(str(self.OUTPUT_DIRECTORY() + self.filename) + '.txt', 'w', encoding='utf-8') as outfile:
            for dataArray in self.arrayOfArraysData:
                for dataItem in dataArray:
                    print(dataItem, file=outfile)
