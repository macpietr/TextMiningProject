import pyLDAvis.gensim
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk import word_tokenize

from matthausITberatung.DataMining.LDA.Utils import Utils
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

class TopicModelling:
#TODO: zrobic dla bigrams i trigrams. dla kazdej linii lotniczej oraz dla wszystkich opinii

    listOfClusters_wholeOpinions = ObjectsManager().getSavedObject('listOfClusters_wholeOpinions')
    dictOfAirlinesClusters = ObjectsManager().getSavedObject('dictOfAirlinesClusters')

    def __tokenizeCluster(self, cluster):
        return [word_tokenize(opinion) for opinion in cluster]


    def displayTopicPlot(self, cluster):
        cluster_tokenized = self.__tokenizeCluster(cluster)
        dictionary = Dictionary(cluster_tokenized)

        corpus = [dictionary.doc2bow(opinion) for opinion in cluster_tokenized]

        Utils().filterCorpus(corpus, dictionary, 0.03)

        lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)

        pyLDAvis.enable_notebook()
        vis = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary, mds="mmds", R=30)
        pyLDAvis.show(vis)