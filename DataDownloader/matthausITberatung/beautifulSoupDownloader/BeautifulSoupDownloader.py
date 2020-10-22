import requests

from bs4 import BeautifulSoup

from matthausITberatung.URLs.URLprovider import URLprovider

text = 'downloaded3'
urlProvider = URLprovider()
listOfWizzAirURLs = urlProvider.getListOfWizzAirURLs(urlProvider.LUFTHANSA())

listOfHTMLtags = ['div']
print(listOfHTMLtags)
with open(str(text) + '.txt', 'w', encoding='utf-8') as outfile:
    for url in listOfWizzAirURLs:
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        text = [' '.join(s.findAll(text=True)) for s in soup.find_all(listOfHTMLtags)]
        for item in text:
            print(item, file=outfile)

        print("Done! File is saved where you have your scrape-website.py")
