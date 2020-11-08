class FileWriter:

    def putExtractedDataIntoFile(self, fileName, extractedData):
        with open(str(fileName) + '.txt', 'w', encoding='utf-8') as outfile:
            for item in extractedData:
                print(item, file=outfile)
