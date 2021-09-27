import re
import string


class DataCleaner:

    def cleanDataExtended(self, data):
        data = data.lower()
        data = re.sub('\[.*?\]', '', data)
        data = re.sub('[%s]' % re.escape(string.punctuation), '', data)
        data = re.sub('\w*\d\w*', '', data)
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
