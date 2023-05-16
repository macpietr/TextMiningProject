from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager


class TfidfUtils:

    def prepareData(self):
        # custom_stop_words = list(ObjectsManager().getSavedObject('STOP_WORDS_LIST_FROM_SHORT_WORDS'))
        listOfWholeOpinions = []
        opinionsPerAirline = {}
        for airline in PathsManager().LIST_OF_AIRLINES:
            airlineOpinions = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR, 'MainUserOpinion', airline)\
                .split('\n')
            perAirlineList = self.__lemmatizeAirLineOpinions(airlineOpinions, listOfWholeOpinions)
            opinionsPerAirline[airline] = perAirlineList
        ObjectsManager().saveObject(listOfWholeOpinions, 'listOfWholeOpinions')
        ObjectsManager().saveObject(opinionsPerAirline, 'opinionsPerAirline')

    def __lemmatizeAirLineOpinions(self, airlineOpinions, listOfWholeOpinions):
        perAirlineList = []
        for opinion in airlineOpinions:
            helperString = DataCleaner().lemmatizeLine(opinion)
            perAirlineList.append(helperString)
            listOfWholeOpinions.append(helperString)
        return perAirlineList

    def showExpectedClustersPlot(self, vectors, title):
        ###optimum number of clusters
        plt.clf()
        means = []
        inertias = []
        for k in range(1, 20):
            kmeans = KMeans(n_clusters=k)
            kmeans.fit(vectors)

            means.append(k)
            inertias.append(kmeans.inertia_)

        plt.title(title)
        plt.plot(means, inertias, 'o-')
        plt.xlabel('number of clusters')
        plt.ylabel('inertia')
        plt.grid(True)
        plt.savefig(str(title).replace(" ","")+".png")
