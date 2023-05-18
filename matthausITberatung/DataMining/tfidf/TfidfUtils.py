from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager


class TfidfUtils:

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
