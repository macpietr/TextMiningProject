import re

from matthausITberatung.dataDownloader.AbstractDownloader import AbstractDownloader


class MainMarkInOpinionDownloader(AbstractDownloader):

    def __init__(self, listOfBeautifulSoupObjects):
        super().__init__(listOfBeautifulSoupObjects)