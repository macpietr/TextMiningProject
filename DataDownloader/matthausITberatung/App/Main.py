from matthausITberatung.URLs.URLprovider import URLprovider
from matthausITberatung.dataDownloader.ReviewRatingDownloader import ReviewRatingDownloader
from matthausITberatung.dataDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader
from matthausITberatung.dataDownloader.MainUserOpinionDownloader import MainUserOpoinionDownloader
from matthausITberatung.dataDownloader.MainMarkInOpinionDownloader import MainMarkInOpinionDownloader
from matthausITberatung.writer.FileWriter import FileWriter

urlProvider = URLprovider()
beautifulSoupDownloader = BeautifulSoupDownloader()

listOfAirLineNames = [urlProvider.LUFTHANSA(), urlProvider.WIZZ_AIR(), urlProvider.RYANAIR()]

for airLineName in listOfAirLineNames:
    listOfAirLineURLs = urlProvider.getListOfAirLineURLs(airLineName)
    listOfBeautifulSoupObjects = beautifulSoupDownloader.getListOfBeautifulSoupObject(listOfAirLineURLs)

    mainUserOpoinionData = MainUserOpoinionDownloader(listOfBeautifulSoupObjects).getDataArrayOfArrays()
    mainMarkInOpinionData = MainMarkInOpinionDownloader(listOfBeautifulSoupObjects).getDataArrayOfArrays()

    aircraftData = ReviewRatingDownloader(listOfBeautifulSoupObjects,'Aircraft').getDataArrayOfArrays()
    typeOfTravellerData = ReviewRatingDownloader(listOfBeautifulSoupObjects,'type_of_traveller').getDataArrayOfArrays()
    seatType = ReviewRatingDownloader(listOfBeautifulSoupObjects, 'cabin_flown').getDataArrayOfArrays()
    route = ReviewRatingDownloader(listOfBeautifulSoupObjects, 'cabin_flown').getDataArrayOfArrays()
    dateFlown = ReviewRatingDownloader(listOfBeautifulSoupObjects, 'date_flown').getDataArrayOfArrays()
    isRecommended = ReviewRatingDownloader(listOfBeautifulSoupObjects, 'recommended').getDataArrayOfArrays()

    FileWriter(airLineName, mainUserOpoinionData, 'MainUserOpinion').putExtractedDataIntoFile()
    FileWriter(airLineName, mainMarkInOpinionData, 'MainMarkInOpinion').putExtractedDataIntoFile()

    FileWriter(airLineName, aircraftData, 'AircraftDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, typeOfTravellerData, 'TypeOfTravellerDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, seatType, 'SeatTypeDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, route, 'RouteDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, dateFlown, 'DateFlownDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, isRecommended, 'IsRecommendedDownloaded').putExtractedDataIntoFile()

    ###TODO: Make analogical sollution of collecting data for ratings with stars

print("Done! File is saved where you have your scrape-website.py")