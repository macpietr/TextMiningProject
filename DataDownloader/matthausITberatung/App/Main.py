from matthausITberatung.URLs.URLprovider import URLprovider
from matthausITberatung.beautifulSoupDownloader.BeautifulSoupDownloader import BeautifulSoupDownloader
from matthausITberatung.beautifulSoupDownloader.MainPostsDownloader import MainPostsDownloader

ariLineName = URLprovider().LUFTHANSA()

listOfAirLineURLs = URLprovider().getListOfAirLineURLs(ariLineName)

listOfBeautifulSoupObjects = BeautifulSoupDownloader().getListOfBeautifulSoupObject(listOfAirLineURLs)

arrayOfUsersOpinionsArrays = []
for beautifulSoupObjects in listOfBeautifulSoupObjects:
    userOpinionArray = MainPostsDownloader().getMainUsersOpinions(beautifulSoupObjects)
    arrayOfUsersOpinionsArrays.append(userOpinionArray)

for userOpinionArray in arrayOfUsersOpinionsArrays:
    for userOpinion in userOpinionArray:
        print(userOpinion)

print("Done! File is saved where you have your scrape-website.py")