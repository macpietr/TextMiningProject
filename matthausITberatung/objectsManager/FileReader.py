class FileReader:

    def readFile(self, parentDir, childDir, airlineName):
        file = open(str(parentDir+'\\'+childDir+'\\'+airlineName+'_'+childDir+'.txt'), 'r', encoding='utf-8')
        return file.read()