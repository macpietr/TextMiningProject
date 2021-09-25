from matthausITberatung.dataDownloader.URLs.URLprovider import URLprovider
from matthausITberatung.dataDownloader.dataDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader
from matthausITberatung.dataDownloader.dataDownloader.MainMarkInOpinionDownloader import MainMarkInOpinionDownloader
from matthausITberatung.dataDownloader.dataDownloader.MainUserOpinionDownloader import MainUserOpoinionDownloader
from matthausITberatung.dataDownloader.dataDownloader.ReviewRatingDownloader import ReviewRatingDownloader
from matthausITberatung.dataDownloader.dataDownloader.ReviewRatingStarDownloader import ReviewRatingStarDownloader
from matthausITberatung.fileManager.FileWriter import FileWriter
from matthausITberatung.fileManager.PathsManager import PathsManager

print('dataDownloader module has started')

beautifulSoupDownloader = BeautifulSoupDownloader()
saveFolder = PathsManager().DOWNLOADED_FILES_DIR()

for airLineName in PathsManager().LIST_OF_AIRLINES():

    print('scraping data for: ' + airLineName)

    listOfAirLineURLs = URLprovider().getListOfAirLineURLs(airLineName)
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

    FileWriter(airLineName, 'MainUserOpinion', saveFolder).putExtractedDataIntoFile(mainUserOpoinionData)
    FileWriter(airLineName, 'MainMarkInOpinion', saveFolder).putExtractedDataIntoFile(mainMarkInOpinionData)

    FileWriter(airLineName, 'Aircraft', saveFolder).putExtractedDataIntoFile(aircraftData)
    FileWriter(airLineName, 'TypeOfTraveller', saveFolder).putExtractedDataIntoFile(typeOfTravellerData)
    FileWriter(airLineName, 'SeatType', saveFolder).putExtractedDataIntoFile(seatType)
    FileWriter(airLineName, 'Route', saveFolder).putExtractedDataIntoFile(route)
    FileWriter(airLineName, 'DateFlown', saveFolder).putExtractedDataIntoFile(dateFlown)
    FileWriter(airLineName, 'IsRecommended', saveFolder).putExtractedDataIntoFile(isRecommended)

    FileWriter(airLineName, 'SeatComfort', saveFolder).putExtractedDataIntoFile(seatComfort)
    FileWriter(airLineName, 'CabinStaffService', saveFolder).putExtractedDataIntoFile(cabinStaffService)
    FileWriter(airLineName, 'FoodAndBeverages', saveFolder).putExtractedDataIntoFile(foodAndBeverages)
    FileWriter(airLineName, 'InflightEntertainment', saveFolder).putExtractedDataIntoFile(inflightEntertainment)
    FileWriter(airLineName, 'GroundService', saveFolder).putExtractedDataIntoFile(groundService)
    FileWriter(airLineName, 'WifiAndConnectivity', saveFolder).putExtractedDataIntoFile(wifiAndConnectivity)
    FileWriter(airLineName, 'ValueForMoney', saveFolder).putExtractedDataIntoFile(valueForMoney)

    print('operation for airline: ' + airLineName + ' is done!')

print("Done! Data is scraped and saved in: " + saveFolder)