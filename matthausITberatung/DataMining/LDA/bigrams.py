import gensim
import pyLDAvis.gensim
from gensim import corpora
from gensim.models import TfidfModel

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

#co ja tutaj w ogóle robię??

# TODO: tutaj są wyrazy, które mają długość 2, trzeba sie pozbyc tych wyrazow i w ogole chyba stopwordsy nie zadzialaly dobrze
listOfWholeOpinions = ObjectsManager().getSavedObject('listOfWholeOpinions')
lemmatizedDataDictOfListsWithoutStopWords = ObjectsManager().getSavedObject(PathsManager().LEMMATIZED_DATA_DICT_OF_LISTS_WITHOUT_STOP_WORDS)

listOfListsOfWholeOpinionsWords = []
for airline in PathsManager().LIST_OF_AIRLINES:
    airlineOpinionsList = lemmatizedDataDictOfListsWithoutStopWords[airline]
    for opinion in airlineOpinionsList:
        listOfListsOfWholeOpinionsWords.append(str(opinion).split(' '))
# for opinion in listOfWholeOpinions:
#     listOfListsOfWholeOpinionsWords.append(str(opinion).split(' '))

# print(listOfWholeOpinions[0])

print(listOfListsOfWholeOpinionsWords[0][0:20])

bigramsPhrases = gensim.models.Phrases(listOfListsOfWholeOpinionsWords, min_count=5, threshold=50)
trigramPhrases = gensim.models.Phrases(bigramsPhrases[listOfListsOfWholeOpinionsWords], threshold=50)
#
bigram = gensim.models.phrases.Phraser(bigramsPhrases)
trigram = gensim.models.phrases.Phraser(trigramPhrases)
#
dataBigrams = [bigram[opinion] for opinion in listOfWholeOpinions]
dataBigramsTrigrams = [trigram[bigram[opinion]] for opinion in listOfListsOfWholeOpinionsWords]

print(dataBigramsTrigrams[0][0:20])

#TF-IDF removal

id2word = corpora.Dictionary(dataBigramsTrigrams)
texts = dataBigramsTrigrams
corpus = [id2word.doc2bow(text) for text in texts]
print(corpus[0][0:20])

tfidf = TfidfModel(corpus, id2word=id2word)

low_value = 0.03

words = []
words_missing_in_tfifd = []

for i in range(0, len(corpus)):
    bow = corpus[i]
    low_value_words = [] #reinitialize to be safe. You can skip this.
    tfidf_ids = [id for id, value in tfidf[bow]]
    bow_ids = [id for id, value in bow]
    low_value_words = [id for id, value in tfidf[bow] if value < low_value]
    words_missing_in_tfidf = [id for id in bow_ids if id not in tfidf_ids] # The words with tf-idf socre 0 will be missing

    new_bow = [b for b in bow if b[0] not in low_value_words and b[0] not in words_missing_in_tfidf]

    #reassign
    corpus[i] = new_bow

print(corpus[0][0:20])

lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                            id2word=id2word,
                                            num_topics=20,
                                            random_state=100,
                                            update_every=1,
                                            chunksize=100,
                                            passes=10,
                                            alpha="auto")

pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word, mds="mmds", R=30)
pyLDAvis.show(vis)

#
# print(dataBigrams)
