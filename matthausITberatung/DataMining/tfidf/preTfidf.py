from matthausITberatung.DataMining.tfidf.TfidfUtils import TfidfUtils
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer

TfidfUtils().prepareData()

opinionsPerAirline = ObjectsManager().getSavedObject('opinionsPerAirline')
listOfWholeOpinions = ObjectsManager().getSavedObject('listOfWholeOpinions')

vectorizer = TfidfVectorizer(
    lowercase=True,
    max_features=100,
    max_df=0.8,
    min_df=5,
    ngram_range=(1,3),
    stop_words=ObjectsManager().getSavedObject(PathsManager().UNION_STOP_WORDS)
)

commondatavectors = vectorizer.fit_transform(listOfWholeOpinions)
ObjectsManager().saveObject(commondatavectors, 'commondatavectors')

for airline in PathsManager().LIST_OF_AIRLINES:
    ObjectsManager().saveObject(vectorizer.fit_transform(opinionsPerAirline[airline]), str(airline)+'vectors')

ObjectsManager().saveObject(vectorizer, 'vectorizer')