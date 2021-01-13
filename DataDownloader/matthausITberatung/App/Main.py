from matthausITberatung.URLs.URLprovider import URLprovider
from matthausITberatung.dataDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader
from matthausITberatung.dataDownloader.MainUserOpinionDownloader import MainUserOpoinionDownloader
from matthausITberatung.writer.FileWriter import FileWriter

urlProvider = URLprovider()
beautifulSoupDownloader = BeautifulSoupDownloader()

listOfAirLineNames = [urlProvider.LUFTHANSA(), urlProvider.WIZZ_AIR(), urlProvider.RYANAIR()]
for airLineName in listOfAirLineNames:
    listOfAirLineURLs = urlProvider.getListOfAirLineURLs(airLineName)
    listOfBeautifulSoupObjects = beautifulSoupDownloader.getListOfBeautifulSoupObject(listOfAirLineURLs)

    FileWriter(airLineName,
               MainUserOpoinionDownloader(listOfBeautifulSoupObjects).getDataArrayOfArrays(),
               'MainUserOpinion').putExtractedDataIntoFile()

print("Done! File is saved where you have your scrape-website.py")
