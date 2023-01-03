class URLprovider:

    def getListOfAirLineURLs(self, airlineName):
        listOfAirLineURLs = []
        #12 pages, because range works like 1 <= x < 13
        for iterator in range(1, 13):
            listOfAirLineURLs.append(URLprovider.getURL(iterator, airlineName))
        return listOfAirLineURLs

    def getURL(iterator, airLineName):
        return "https://www.airlinequality.com/airline-reviews/"\
               +airLineName+"/page/"+str(iterator)+"/?sortby=post_date%3ADesc&pagesize=100"