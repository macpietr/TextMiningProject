class FileWriter:

    def putExtractedDataIntoFile(self, fileName, arrayOfArraysData):
        with open(str(fileName) + '.txt', 'w', encoding='utf-8') as outfile:
            for dataArray in arrayOfArraysData:
                for dataItem in dataArray:
                    print(dataItem, file=outfile)
