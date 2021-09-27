import re
import string


class DataCleaner:

    def cleanDataExtended(self, data):
        data = data.lower()
        data = re.sub('[%s]' % re.escape(string.punctuation), '', data) #remove interpunction
        data = re.sub('[''""...]', '', data)
        data = re.sub('\w*\d\w*', '', data) #remove numbers
        data = re.sub('\n', '', data)
        return data

    def cleanData(self, data):
        return data\
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
