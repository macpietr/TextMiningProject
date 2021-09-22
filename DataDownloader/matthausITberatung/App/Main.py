from DataDownloader.matthausITberatung.URLs.URLprovider import URLprovider
from DataDownloader.matthausITberatung.dataDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader
from DataDownloader.matthausITberatung.dataDownloader.MainMarkInOpinionDownloader import MainMarkInOpinionDownloader
from DataDownloader.matthausITberatung.dataDownloader.MainUserOpinionDownloader import MainUserOpoinionDownloader
from DataDownloader.matthausITberatung.dataDownloader.ReviewRatingDownloader import ReviewRatingDownloader
from DataDownloader.matthausITberatung.dataDownloader.ReviewRatingStarDownloader import ReviewRatingStarDownloader
from DataDownloader.matthausITberatung.writer.FileWriter import FileWriter

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

    seatComfort = ReviewRatingStarDownloader(listOfBeautifulSoupObjects, 'seat_comfort').getDataArrayOfArrays()
    cabinStaffService = ReviewRatingStarDownloader(listOfBeautifulSoupObjects, 'cabin_staff_service').getDataArrayOfArrays()
    foodAndBeverages = ReviewRatingStarDownloader(listOfBeautifulSoupObjects, 'food_and_beverages').getDataArrayOfArrays()
    inflightEntertainment = ReviewRatingStarDownloader(listOfBeautifulSoupObjects, 'inflight_entertainment').getDataArrayOfArrays()
    groundService = ReviewRatingStarDownloader(listOfBeautifulSoupObjects, 'ground_service').getDataArrayOfArrays()
    wifiAndConnectivity = ReviewRatingStarDownloader(listOfBeautifulSoupObjects, 'wifi_and_connectivity').getDataArrayOfArrays()
    valueForMoney = ReviewRatingStarDownloader(listOfBeautifulSoupObjects, 'value_for_money').getDataArrayOfArrays()

    FileWriter(airLineName, mainUserOpoinionData, 'MainUserOpinion').putExtractedDataIntoFile()
    FileWriter(airLineName, mainMarkInOpinionData, 'MainMarkInOpinion').putExtractedDataIntoFile()

    FileWriter(airLineName, aircraftData, 'AircraftDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, typeOfTravellerData, 'TypeOfTravellerDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, seatType, 'SeatTypeDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, route, 'RouteDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, dateFlown, 'DateFlownDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, isRecommended, 'IsRecommendedDownloaded').putExtractedDataIntoFile()

    FileWriter(airLineName, seatComfort, 'SeatComfortDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, cabinStaffService, 'CabinStaffServiceDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, foodAndBeverages, 'FoodAndBeveragesDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, inflightEntertainment, 'InflightEntertainmentDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, groundService, 'GroundServiceDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, wifiAndConnectivity, 'WifiAndConnectivityDownloaded').putExtractedDataIntoFile()
    FileWriter(airLineName, valueForMoney, 'ValueForMoneyDownloaded').putExtractedDataIntoFile()

print("Done! File is saved where you have your scrape-website.py")