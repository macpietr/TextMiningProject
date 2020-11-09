class FileWriter:

    def PROJECT_DIRECTORY(self):
        return 'C:\\Users\\macpi\\Dokumenty\\magisterka\\PythonProjects\\DataDownloader\\output_files\\'
    def putExtractedDataIntoFile(self, fileName, arrayOfArraysData):
        with open(str(self.PROJECT_DIRECTORY() + fileName) + '.txt', 'w', encoding='utf-8') as outfile:
            for dataArray in arrayOfArraysData:
                for dataItem in dataArray:
                    print(dataItem, file=outfile)
