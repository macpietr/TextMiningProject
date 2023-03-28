from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.topicModelling2.tfidf.TfidfUtils import TfidfUtils
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
    stop_words=text.ENGLISH_STOP_WORDS
        .union(list(ObjectsManager().getSavedObject(PathsManager().STOP_WORDS_LIST_FROM_SHORT_WORDS)))
        .union(['dont'])
)

commondatavectors = vectorizer.fit_transform(listOfWholeOpinions)
ObjectsManager().saveObject(commondatavectors, 'commondatavectors')

for airline in PathsManager().LIST_OF_AIRLINES:
    ObjectsManager().saveObject(vectorizer.fit_transform(opinionsPerAirline[airline]), str(airline)+'vectors')

ObjectsManager().saveObject(vectorizer, 'vectorizer')