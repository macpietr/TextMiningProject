import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

airlines = PathsManager().LIST_OF_AIRLINES

# our desired number of clusters
numberOfClusters = 3

components = airlines
# components.append('commondata')

dictOfDictOfAirlnesClusters = {}
for component in components:
    plt.clf()
    vectorizer = ObjectsManager().getSavedObject('vectorizer')
    vectors = ObjectsManager().getSavedObject(component + 'vectors')
    feature_names = vectorizer.get_feature_names()
    model = KMeans(n_clusters=numberOfClusters, n_init=1, max_iter=100, init="k-means++")
    model.fit(vectors)
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    print("######## " + component + " #########")
    dictOfClusters = {}
    for i in range(numberOfClusters):
        print("cluster " + str(i) + "\n")
        for centorid in order_centroids[i, :20]:
            print(feature_names[centorid])
        print("\n")
        helperList = []
        for centorid in order_centroids[i]:
            helperList.append(feature_names[centorid])
        dictOfClusters[i] = helperList

    dictOfDictOfAirlnesClusters[component] = dictOfClusters

    kMeanIndices = model.fit_predict(vectors)
    pca = PCA(n_components=2)
    scatterPlotPoints = pca.fit_transform(vectors.toarray())
    xAxis = [pointX[0] for pointX in scatterPlotPoints]
    yAxis = [pointY[1] for pointY in scatterPlotPoints]
    colors = ["r", "b", "c", "y", "m"]
    plt.scatter(x=xAxis, y=yAxis, c=[colors[d] for d in kMeanIndices], s=10)
    plt.title(component)
    plt.savefig(str(component) + ".png")

ObjectsManager().saveObject(dictOfDictOfAirlnesClusters, 'dictOfDictOfAirlnesClusters')

print("\n")
print("####### TF-IDF finished######")
