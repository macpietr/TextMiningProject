class FileReader:

    def readFile(self, parentDir, childDir, airlineName):
        file = open(parentDir+'\\'+childDir+'\\'+airlineName+'_'+childDir+'.txt', 'r', encoding='utf-8')
        return file.read()