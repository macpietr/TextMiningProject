
class GeneralDataCleaner:


    def __init__(self, processingString):
        self.processingString = processingString


    def cleanData(self):
        return self.processingString\
            .replace('\\n','')\
            .replace('\\r','')\
            .replace('\\xa0','')\
            .replace('\\','')\
            .replace('[','')\
            .replace(']','')\
            .replace('"','')\
            .replace('\'','')\
            .replace('ttttttttttttt','')\
            .rstrip()\
            .lstrip()
