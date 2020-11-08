from matthausITberatung.URLs.URLprovider import URLprovider
from matthausITberatung.beautifulSoupDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader
from matthausITberatung.beautifulSoupDownloader.MainPostsDownloader import MainPostsDownloader
from matthausITberatung.writer.FileWriter import FileWriter

urlProvider = URLprovider()
beautifulSoupDownloader = BeautifulSoupDownloader()
mainPostsDownloader = MainPostsDownloader()
fileWriter = FileWriter()


airLineName = urlProvider.LUFTHANSA()

listOfAirLineURLs = urlProvider.getListOfAirLineURLs(airLineName)

listOfBeautifulSoupObjects = beautifulSoupDownloader.getListOfBeautifulSoupObject(listOfAirLineURLs)

arrayOfUsersOpinionsArrays = []
for beautifulSoupObjects in listOfBeautifulSoupObjects:
    userOpinionArray = mainPostsDownloader.getMainUsersOpinions(beautifulSoupObjects)
    arrayOfUsersOpinionsArrays.append(userOpinionArray)

fileName = 'MainOpinions'

fileWriter.putExtractedDataIntoFile(fileName,arrayOfUsersOpinionsArrays)

#TODO implement FileWriter class

print("Done! File is saved where you have your scrape-website.py")