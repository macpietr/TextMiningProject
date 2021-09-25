from matthausITberatung.dataDownloader.URLs.URLprovider import URLprovider
from matthausITberatung.dataDownloader.dataDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader
from matthausITberatung.dataDownloader.dataDownloader.MainMarkInOpinionDownloader import MainMarkInOpinionDownloader
from matthausITberatung.dataDownloader.dataDownloader.MainUserOpinionDownloader import MainUserOpoinionDownloader
from matthausITberatung.dataDownloader.dataDownloader.ReviewRatingDownloader import ReviewRatingDownloader
from matthausITberatung.dataDownloader.dataDownloader.ReviewRatingStarDownloader import ReviewRatingStarDownloader
from matthausITberatung.fileManager.FileWriter import FileWriter
from matthausITberatung.fileManager.PathsManager import PathsManager

print('dataDownloader module has started')

urlProvider = URLprovider()
beautifulSoupDownloader = BeautifulSoupDownloader()
saveFolder = PathsManager().DOWNLOADED_FILES_DIR()

listOfAirLineNames = [urlProvider.LUFTHANSA(), urlProvider.WIZZ_AIR(), urlProvider.RYANAIR()]

for airLineName in listOfAirLineNames:

    print('scraping data for: ' + airLineName)

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

    print('saving data for: ' + airLineName)

    FileWriter(airLineName, mainUserOpoinionData, 'MainUserOpinion', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, mainMarkInOpinionData, 'MainMarkInOpinion', saveFolder).putExtractedDataIntoFile()

    FileWriter(airLineName, aircraftData, 'AircraftDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, typeOfTravellerData, 'TypeOfTravellerDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, seatType, 'SeatTypeDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, route, 'RouteDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, dateFlown, 'DateFlownDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, isRecommended, 'IsRecommendedDownloaded', saveFolder).putExtractedDataIntoFile()

    FileWriter(airLineName, seatComfort, 'SeatComfortDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, cabinStaffService, 'CabinStaffServiceDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, foodAndBeverages, 'FoodAndBeveragesDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, inflightEntertainment, 'InflightEntertainmentDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, groundService, 'GroundServiceDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, wifiAndConnectivity, 'WifiAndConnectivityDownloaded', saveFolder).putExtractedDataIntoFile()
    FileWriter(airLineName, valueForMoney, 'ValueForMoneyDownloaded', saveFolder).putExtractedDataIntoFile()

    print('operation for airline: ' + airLineName + ' is done!')

print("Done! Data is scraped and saved in: " + saveFolder)