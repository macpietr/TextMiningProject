class URLprovider:

    def WIZZ_AIR(self):
        return 'wizz-air'

    def RAYANAIR(self):
        return 'rayanair'

    def LUFTHANSA(self):
        return 'lufthansa'

    def getURL(iterator, airLineName):
        return "https://www.airlinequality.com/airline-reviews/"+airLineName+"/page/"+str(iterator)+"/?sortby=post_date%3ADesc&pagesize=100"

    def getListOfWizzAirURLs(self, airlineName):
        listOfWizzAirURLs = []
        for iterator in range(1, 11):
            listOfWizzAirURLs.append(URLprovider.getURL(iterator, airlineName))
        return listOfWizzAirURLs
