import pickle

from sklearn.feature_extraction.text import CountVectorizer
from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.fileManager.FileReader import FileReader
from matthausITberatung.fileManager.PathsManager import PathsManager
import pandas as pd

cleanedDataMap = {}
for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES()):
    downloadedData = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR(),'MainUserOpinion',airline)
    cleanedDataMap[airline] = DataCleaner().cleanData(downloadedData)

print(cleanedDataMap.keys())

#nie wiem do czego to ale chyba potrzebne - nie wiem czym się różni mapa poniżej od mapy powyżej
prepareDataForCorpus = {key: [cleanedDataMap[key]] for (key,value) in cleanedDataMap.items()}

pd.set_option('max_colwidth',400)

corpus = pd.DataFrame.from_dict(prepareDataForCorpus).transpose()
corpus.columns = ['opinions']
corpus = corpus.sort_index()

print(corpus)
#Add next column to corpus
corpus['airlines'] = PathsManager().LIST_OF_AIRLINES()

print(corpus)
#Pickle the corpus
corpus.to_pickle(PathsManager().PICKLED_FILES()+"/corpus.pkl")

#Document-Term Matrix
cv = CountVectorizer(stop_words='english') #declare CountVectorizer
data_cv = cv.fit_transform(corpus.opinions) #fit declared CountVectorizer to my opinions data
#make an array where columns are labeled as words appeared in opinions and rows are labeled as certain arilines.
#Values of matrix show quantity of word in opinions for certain airline
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names_out())
#pickle Document-Term Matrix
data_dtm.index = corpus.index

print(data_dtm)

data_dtm.to_pickle(PathsManager().PICKLED_FILES()+"/dtm.pkl")


pickle.dump(cv, open("corpus.pkl", "wb"))