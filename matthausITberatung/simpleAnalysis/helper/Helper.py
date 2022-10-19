class Helper:

    def createDictOfLists(self, clearedDictOfStrings):
        dictOfLists = {}
        for key in clearedDictOfStrings.keys():
            dictOfLists[key] = clearedDictOfStrings[key].split(' ')
            self.__removeEmpties(dictOfLists[key])
        return dictOfLists

    def convertStringsToInts(self, dictOfLists):
        dictOfInts = {}
        for key in dictOfLists.keys():
            dictOfInts[key] = list(map(int,dictOfLists[key]))
        return dictOfInts

    def __removeEmpties(self, list):
        for term in list:
            if term == '':
                list.remove(term)