class URLprovider:

    def WIZZ_AIR(self):
        return 'wizz-air'

    def RAYANAIR(self):
        return 'rayanair'

    def LUFTHANSA(self):
        return 'lufthansa'

    def getListOfAirLineURLs(self, airlineName):
        listOfAirLineURLs = []
        for iterator in range(1, 11):
            listOfAirLineURLs.append(URLprovider.getURL(iterator, airlineName))
        return listOfAirLineURLs

    def getURL(iterator, airLineName):
        return "https://www.airlinequality.com/airline-reviews/"+airLineName+"/page/"+str(iterator)+"/?sortby=post_date%3ADesc&pagesize=100"