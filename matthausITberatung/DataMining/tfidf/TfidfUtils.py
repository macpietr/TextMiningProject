from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


class TfidfUtils:

    def showExpectedClustersPlot(self, vectors, title):
        ###optimum number of clusters = 3
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
