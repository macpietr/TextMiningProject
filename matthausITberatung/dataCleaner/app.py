import pickle
from collections import Counter

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer

from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.PathsManager import PathsManager
import pandas as pd

cleanedDataMap = {}
for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES):
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
corpus['airlines'] = PathsManager().LIST_OF_AIRLINES

print(corpus)
#Pickle the corpus
corpus.to_pickle(PathsManager().PICKLED_FILES+"/corpus.pkl")

#Document-Term Matrix
cv = CountVectorizer(stop_words='english') #declare CountVectorizer
data_cv = cv.fit_transform(corpus.opinions) #fit declared CountVectorizer to my opinions data
#make an array where columns are labeled as words appeared in opinions and rows are labeled as certain arilines.
#Values of matrix show quantity of word in opinions for certain airline
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names_out())
#pickle Document-Term Matrix
data_dtm.index = corpus.index

print(data_dtm)

data_dtm.to_pickle(PathsManager().PICKLED_FILES+"/dtm.pkl")


pickle.dump(cv, open("corpus.pkl", "wb"))

#Top words using DTM

data_dtm = data_dtm.transpose()
print(data_dtm.head())

#Top 30 words for every airline

top_dict = {}
for column in data_dtm.columns:
    top = data_dtm[column].sort_values(ascending=False).head(30)
    top_dict[column] = list(zip(top.index, top.values))

print(top_dict)

for airline, top_words in top_dict.items():
    print(airline)
    print(', '.join([word for word, count in top_words[0:14]]))
    print('---')

#Add new stop words. words which appears to many times don't tell us anything

words = []
for airline in data_dtm.columns:
    top = [word for (word, count) in top_dict[airline]]
    for top_word in top:
        words.append(top_word)

print(words)

print(Counter(words).most_common())


#TODO: te stop wordsy to trzeba będzie zmienić, bo nie wszystkie z wyrazów będą się do nich zaliczać, niektóre rzeczywiście będzie można wywalić
# w przypadku analizy porównawczej, ale wpierw muszę przepowadzić analizę ogólną
add_stop_words = [word for word,count in Counter(words).most_common() if count > 2]
print(add_stop_words)

###########

# corpus = pd.read_pickle(PathsManager().PICKLED_FILES+'/corpus.pkl')
print(corpus)

stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)

print(stop_words)

##Recreate DTM

cv = CountVectorizer(stop_words=stop_words)
data_cv = cv.fit_transform(corpus.opinions)
data_stop = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names_out())
data_stop.index = corpus.index
print(data_stop)

pickle.dump(cv,open(PathsManager().PICKLED_FILES+'/cv_stop.pkl','wb'))
data_stop.to_pickle('dtm_stop.pkl')

print(data_stop)

##word clouds