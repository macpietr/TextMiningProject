from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from sklearn.feature_extraction.text import TfidfVectorizer

opinionsPerAirline = ObjectsManager().getSavedObject('dataDictOfClearedOpinions')
# opinionsPerAirline = ObjectsManager().getSavedObject('dictOfBigramedOpinions')
# listOfWholeOpinions = ObjectsManager().getSavedObject('listOfWholeOpinions')

vectorizer = TfidfVectorizer(
    lowercase=True,
    max_features=2000,
    max_df=0.8,
    min_df=5,
    ngram_range=(1,3),
    stop_words=ObjectsManager().getSavedObject(PathsManager().UNION_STOP_WORDS)
)

# commondatavectors = vectorizer.fit_transform(listOfWholeOpinions)
# ObjectsManager().saveObject(commondatavectors, 'commondatavectors')

for airline in PathsManager().LIST_OF_AIRLINES:
    ObjectsManager().saveObject(vectorizer.fit_transform(opinionsPerAirline[airline]), str(airline)+'vectors')

ObjectsManager().saveObject(vectorizer, 'vectorizer')

print('Finished')