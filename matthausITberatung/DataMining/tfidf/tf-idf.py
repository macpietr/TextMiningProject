import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

airlines = PathsManager().LIST_OF_AIRLINES

# our desired number of clusters
numberOfClusters = 4

opinionsPerAirline = ObjectsManager().getSavedObject('dataDictOfClearedOpinions')

dictOfDictOfAirlnesClusters = {}
dictOfDictsOfAirlinesClustersOpinions = {}
vectorizer = ObjectsManager().getSavedObject('vectorizer')
for airline in airlines:
    plt.clf()
    vectors = vectorizer.fit_transform(opinionsPerAirline[airline])
    # vectors = ObjectsManager().getSavedObject(airline + 'vectors')
    feature_names = vectorizer.get_feature_names()
    k_means = KMeans(n_clusters=numberOfClusters, n_init=1, max_iter=100, init="k-means++")
    k_means.fit(vectors)
    clusters = k_means.labels_
    df = pd.DataFrame({'opinion': opinionsPerAirline[airline], 'cluster': clusters})
    # Create dict where cluster number is key and list of opinions is value
    # add this dict as a value of bigger dict
    dictOfDictsOfAirlinesClustersOpinions[airline] = df.groupby('cluster')['opinion'].apply(list).to_dict()
    order_centroids = k_means.cluster_centers_.argsort()[:, ::-1]
    print("######## " + airline + " #########")
    dictOfClusters = {}
    for i in range(numberOfClusters):
        print("cluster " + str(i) + "\n")
        for centorid in order_centroids[i, :20]:
            print(feature_names[centorid])
        print("\n")

    kMeanIndices = k_means.fit_predict(vectors)
    pca = PCA(n_components=2)
    scatterPlotPoints = pca.fit_transform(vectors.toarray())
    xAxis = [pointX[0] for pointX in scatterPlotPoints]
    yAxis = [pointY[1] for pointY in scatterPlotPoints]
    colors = ["r", "b", "c", "y", "m"]
    plt.scatter(x=xAxis, y=yAxis, c=[colors[d] for d in kMeanIndices], s=10)
    plt.title(airline)
    plt.show()

ObjectsManager().saveObject(dictOfDictsOfAirlinesClustersOpinions, 'dictOfDictsOfAirlinesClustersOpinions')

print("\n")
print("####### TF-IDF finished######")
