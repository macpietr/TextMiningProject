from abc import abstractmethod


class AbstractDownloader:

    def __init__(self, listOfBeautifulSoupObjects):
        self.listOfBeautifulSoupObjects = listOfBeautifulSoupObjects

    def getDataArrayOfArrays(self):
        dataArrayOfArrays = []
        for beautifulSoupObjects in self.listOfBeautifulSoupObjects:
            dataArrayOfArrays.append(self.getDataArray(beautifulSoupObjects))
        return dataArrayOfArrays

    def getDataArray(self, beautifulSoupObject):
        dataArray = []
        for item in self.getDataBasedOnHTMLtype(beautifulSoupObject):
            dataArray.append(self.getProcessedRow(self.getExtractedRow(item)))
        return dataArray

    @abstractmethod
    def getDataBasedOnHTMLtype(self, beautifulSoupObject):
        pass

    @abstractmethod
    def getProcessedRow(self, extractedRow):
        pass

    @abstractmethod
    def getExtractedRow(self, item):
        pass