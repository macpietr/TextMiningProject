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

    FileWriter(saveFolder, 'MainUserOpinion', airLineName).putExtractedDataIntoFile(mainUserOpoinionData)
    FileWriter(saveFolder, 'MainMarkInOpinion', airLineName).putExtractedDataIntoFile(mainMarkInOpinionData)

    FileWriter(saveFolder, 'Aircraft', airLineName).putExtractedDataIntoFile(aircraftData)
    FileWriter(saveFolder, 'TypeOfTraveller', airLineName).putExtractedDataIntoFile(typeOfTravellerData)
    FileWriter(saveFolder, 'SeatType', airLineName).putExtractedDataIntoFile(seatType)
    FileWriter(saveFolder, 'Route', airLineName).putExtractedDataIntoFile(route)
    FileWriter(saveFolder, 'DateFlown', airLineName).putExtractedDataIntoFile(dateFlown)
    FileWriter(saveFolder, 'IsRecommended', airLineName).putExtractedDataIntoFile(isRecommended)

    FileWriter(saveFolder, 'SeatComfort', airLineName).putExtractedDataIntoFile(seatComfort)
    FileWriter(saveFolder, 'CabinStaffService', airLineName).putExtractedDataIntoFile(cabinStaffService)
    FileWriter(saveFolder, 'FoodAndBeverages', airLineName).putExtractedDataIntoFile(foodAndBeverages)
    FileWriter(saveFolder, 'InflightEntertainment', airLineName).putExtractedDataIntoFile(inflightEntertainment)
    FileWriter(saveFolder, 'GroundService', airLineName).putExtractedDataIntoFile(groundService)
    FileWriter(saveFolder, 'WifiAndConnectivity', airLineName).putExtractedDataIntoFile(wifiAndConnectivity)
    FileWriter(saveFolder, 'ValueForMoney', airLineName).putExtractedDataIntoFile(valueForMoney)

    print('operation for airline: ' + airLineName + ' is done!')

print("Done! Data is scraped and saved in: " + saveFolder)