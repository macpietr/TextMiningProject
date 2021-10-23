from matthausITberatung.dataDownloader.URLs.URLprovider import URLprovider
from matthausITberatung.dataDownloader.dataDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader
from matthausITberatung.dataDownloader.dataDownloader.MainMarkInOpinionDownloader import MainMarkInOpinionDownloader
from matthausITberatung.dataDownloader.dataDownloader.MainUserOpinionDownloader import MainUserOpoinionDownloader
from matthausITberatung.dataDownloader.dataDownloader.ReviewRatingDownloader import ReviewRatingDownloader
from matthausITberatung.dataDownloader.dataDownloader.ReviewRatingStarDownloader import ReviewRatingStarDownloader
from matthausITberatung.dataDownloader.dataDownloader.TitleOfOpinionDownloader import TitleOfOpinionDownloader
from matthausITberatung.objectsManager.FileWriter import FileWriter
from matthausITberatung.objectsManager.PathsManager import PathsManager

print('dataDownloader module has started')

beautifulSoupDownloader = BeautifulSoupDownloader()
saveFolder = PathsManager().DOWNLOADED_FILES_DIR()

for airLineName in PathsManager().LIST_OF_AIRLINES():

    print('scraping data for: ' + airLineName)

    listOfAirLineURLs = URLprovider().getListOfAirLineURLs(airLineName)
    listOfBeautifulSoupObjects = beautifulSoupDownloader.getListOfBeautifulSoupObject(listOfAirLineURLs)

    titleOfOpinionData = TitleOfOpinionDownloader(listOfBeautifulSoupObjects).getDataArrayOfArrays()
    mainUserOpinionData = MainUserOpoinionDownloader(listOfBeautifulSoupObjects).getDataArrayOfArrays()
    mainMarkInOpinionData = MainMarkInOpinionDownloader(listOfBeautifulSoupObjects).getDataArrayOfArrays()

    aircraftData = ReviewRatingDownloader(listOfBeautifulSoupObjects,'Aircraft').getDataArrayOfArrays()
    typeOfTravellerData = ReviewRatingDownloader(listOfBeautifulSoupObjects,'type_of_traveller').getDataArrayOfArrays()
    seatType = ReviewRatingDownloader(listOfBeautifulSoupObjects, 'cabin_flown').getDataArrayOfArrays()
    route = ReviewRatingDownloader(listOfBeautifulSoupObjects, 'route').getDataArrayOfArrays()
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

    FileWriter(saveFolder, 'TitleOfOpinion', airLineName).putWebScrappedDataIntoFile(titleOfOpinionData)
    FileWriter(saveFolder, 'MainUserOpinion', airLineName).putWebScrappedDataIntoFile(mainUserOpinionData)
    FileWriter(saveFolder, 'MainMarkInOpinion', airLineName).putWebScrappedDataIntoFile(mainMarkInOpinionData)

    FileWriter(saveFolder, 'Aircraft', airLineName).putWebScrappedDataIntoFile(aircraftData)
    FileWriter(saveFolder, 'TypeOfTraveller', airLineName).putWebScrappedDataIntoFile(typeOfTravellerData)
    FileWriter(saveFolder, 'SeatType', airLineName).putWebScrappedDataIntoFile(seatType)
    FileWriter(saveFolder, 'Route', airLineName).putWebScrappedDataIntoFile(route)
    FileWriter(saveFolder, 'DateFlown', airLineName).putWebScrappedDataIntoFile(dateFlown)
    FileWriter(saveFolder, 'IsRecommended', airLineName).putWebScrappedDataIntoFile(isRecommended)

    FileWriter(saveFolder, 'SeatComfort', airLineName).putWebScrappedDataIntoFile(seatComfort)
    FileWriter(saveFolder, 'CabinStaffService', airLineName).putWebScrappedDataIntoFile(cabinStaffService)
    FileWriter(saveFolder, 'FoodAndBeverages', airLineName).putWebScrappedDataIntoFile(foodAndBeverages)
    FileWriter(saveFolder, 'InflightEntertainment', airLineName).putWebScrappedDataIntoFile(inflightEntertainment)
    FileWriter(saveFolder, 'GroundService', airLineName).putWebScrappedDataIntoFile(groundService)
    FileWriter(saveFolder, 'WifiAndConnectivity', airLineName).putWebScrappedDataIntoFile(wifiAndConnectivity)
    FileWriter(saveFolder, 'ValueForMoney', airLineName).putWebScrappedDataIntoFile(valueForMoney)

    print('operation for airline: ' + airLineName + ' is done!')

print("Done! Data is scraped and saved in: " + saveFolder)