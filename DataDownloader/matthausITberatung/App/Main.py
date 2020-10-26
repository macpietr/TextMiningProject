from matthausITberatung.URLs.URLprovider import URLprovider
from matthausITberatung.beautifulSoupDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader

fileName='downloaded1'
listOfHTMLtags = ['div']

airlineName = URLprovider().LUFTHANSA()

lufthansaURLs = URLprovider().getListOfAirLineURLs(airlineName)

BeautifulSoupDownloader().putExtractedDataIntoFile(fileName,listOfHTMLtags,lufthansaURLs)

print("Done! File is saved where you have your scrape-website.py")