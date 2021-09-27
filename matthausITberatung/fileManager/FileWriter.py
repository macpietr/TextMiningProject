import os


class FileWriter:

    def __init__(self, parentDirectoryName, childDirectoryName, airLineName):
        self.filename = airLineName + '_' + childDirectoryName
        self.childDirectoryName = childDirectoryName
        self.parentDirectoryName = parentDirectoryName

    def OUTPUT_DIRECTORY(self):
        path = self.parentDirectoryName
        if not (os.path.exists(path)):
            os.mkdir(path)
        path = path + '\\' + self.childDirectoryName
        if not (os.path.exists(path)):
            os.mkdir(path)
        return path+'\\'

    def putWebScrappedDataIntoFile(self, arrayOfArraysData):
        with open(str(self.OUTPUT_DIRECTORY() + self.filename) + '.txt', 'w', encoding='utf-8') as outfile:
            for dataArray in arrayOfArraysData:
                for dataItem in dataArray:
                    print(dataItem, file=outfile)

    def putDataIntoFile(self, data):
        with open(str(self.OUTPUT_DIRECTORY() + self.filename) + '.txt', 'w', encoding='utf-8') as outfile:
            print(data, file=outfile)