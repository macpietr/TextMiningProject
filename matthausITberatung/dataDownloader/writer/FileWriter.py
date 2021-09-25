import os


class FileWriter:

    def __init__(self, airLineName, arrayOfArraysData, filenameSuffix):
        self.arrayOfArraysData = arrayOfArraysData
        self.directoryName = filenameSuffix
        self.filename = airLineName + '_' + filenameSuffix

    def OUTPUT_DIRECTORY(self):
        path = 'C:\\Users\\macie\\Documents\\TextMiningProject\\matthausITberatung\\output_files\\' + self.directoryName
        if not (os.path.exists(path)):
            os.mkdir(path)
        return path+'\\'

    def putExtractedDataIntoFile(self):
        with open(str(self.OUTPUT_DIRECTORY() + self.filename) + '.txt', 'w', encoding='utf-8') as outfile:
            for dataArray in self.arrayOfArraysData:
                for dataItem in dataArray:
                    print(dataItem, file=outfile)
