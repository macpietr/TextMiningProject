import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.feature_extraction import text

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager


class ClusterCreator:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            max_features=100,
            max_df=0.8,
            min_df=5,
            ngram_range=(1, 3),
            stop_words=ObjectsManager().getSavedObject(PathsManager().UNION_STOP_WORDS)
        )

    def tfidf_createClusters(self, listOfOpinions):
        tfidf = self.vectorizer.fit_transform(listOfOpinions)
        k_means = KMeans(n_clusters=3)
        k_means.fit(tfidf)
        clusters = k_means.labels_
        df = pd.DataFrame({'opinion': listOfOpinions, 'cluster': clusters})
        return df.groupby('cluster')['opinion'].apply(list)


# listOfWholeOpinions = ObjectsManager().getSavedObject('listOfWholeOpinions')
# lemmatizedDataDictOfListsWithoutStopWords = ObjectsManager().getSavedObject(
#     PathsManager().LEMMATIZED_DATA_DICT_OF_LISTS_WITHOUT_STOP_WORDS)
#
# listOfWholeOpinions_lemmatizedWords = []
# for airline in PathsManager().LIST_OF_AIRLINES:
#     airlineOpinionsList = lemmatizedDataDictOfListsWithoutStopWords[airline]
#     for opinion in airlineOpinionsList:
#         listOfWholeOpinions_lemmatizedWords.append(str(opinion))
#
#
# ObjectsManager().saveObject(tfidf_createClusters(listOfWholeOpinions_lemmatizedWords), 'listOfClusters_wholeOpinions')
#
# dictOfAirlinesClusters = {}
# for airline in PathsManager().LIST_OF_AIRLINES:
#     dictOfAirlinesClusters[airline] = tfidf_createClusters(listOfWholeOpinions_lemmatizedWords)
#
# ObjectsManager().saveObject(dictOfAirlinesClusters, 'dictOfAirlinesClusters')
