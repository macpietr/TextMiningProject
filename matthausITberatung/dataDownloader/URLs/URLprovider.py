class URLprovider:

    def getListOfAirLineURLs(self, airlineName):
        listOfAirLineURLs = []
        # TODO change range for iterator
        for iterator in range(1, 11):
            listOfAirLineURLs.append(URLprovider.getURL(iterator, airlineName))
        return listOfAirLineURLs

    def getURL(iterator, airLineName):
        return "https://www.airlinequality.com/airline-reviews/"\
               +airLineName+"/page/"+str(iterator)+"/?sortby=post_date%3ADesc&pagesize=100"