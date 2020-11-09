from matthausITberatung.URLs.URLprovider import URLprovider
from matthausITberatung.dataDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader
from matthausITberatung.dataDownloader.MainPostsDownloader import MainPostsDownloader
from matthausITberatung.writer.FileWriter import FileWriter

urlProvider = URLprovider()
beautifulSoupDownloader = BeautifulSoupDownloader()
mainPostsDownloader = MainPostsDownloader()
fileWriter = FileWriter()

listOfAirLineNames = [urlProvider.LUFTHANSA(), urlProvider.WIZZ_AIR(), urlProvider.RYANAIR()]
for airLineName in listOfAirLineNames:
    listOfAirLineURLs = urlProvider.getListOfAirLineURLs(airLineName)
    listOfBeautifulSoupObjects = beautifulSoupDownloader.getListOfBeautifulSoupObject(listOfAirLineURLs)
    wholeMainUsersOpinionsArrayOfArrays = mainPostsDownloader.getWholeMainUsersOpinionsArrayOfArrays(listOfBeautifulSoupObjects)
    fileName = airLineName + '_MainOpinions'
    fileWriter.putExtractedDataIntoFile(fileName, wholeMainUsersOpinionsArrayOfArrays)

print("Done! File is saved where you have your scrape-website.py")