import requests

from com.matthausITberatung.receiveData.URLprovider import URLprovider

from bs4 import BeautifulSoup

text = 'downloaded3'
urlProvider = URLprovider()
listOfWizzAirURLs = urlProvider.getListOfWizzAirURLs(urlProvider.LUFTHANSA())

list = ['div']
print(list)
with open(str(text) + '.txt', 'w', encoding='utf-8') as outfile:
    for url in listOfWizzAirURLs:
        website = requests.get(url)
        soup = BeautifulSoup(website.content, "html.parser")
        tags = soup.find_all(list)
        text = [' '.join(s.findAll(text=True)) for s in tags]
        textLen = len(text)

        for item in text:
            print(item, file=outfile)

        print("Done! File is saved where you have your scrape-website.py")
