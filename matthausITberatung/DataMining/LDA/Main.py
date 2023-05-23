import pandas as pd
from gensim.models import LdaModel
from nltk import word_tokenize

from matthausITberatung.DataMining.LDA.TopicModelling import TopicModelling
from matthausITberatung.DataMining.LDA.Utils import Utils
from matthausITberatung.DataMining.tfidf.clustering.ClusterCreator import ClusterCreator
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from gensim.corpora import Dictionary
from gensim.matutils import Sparse2Corpus

#wyczyścić to ze stopWordsow
objectsManager = ObjectsManager()
clusterCreator = ClusterCreator()
topicModelling = TopicModelling()

opinionsPerAirline = objectsManager.getSavedObject('opinionsPerAirline')
listOfWholeOpinions = objectsManager.getSavedObject('listOfWholeOpinions')


#TODO: cos znowu jest nie tak ze stopWordsami - temu powinienem się dobrze przyjrzeć i stworzyć zbiór ostateczny dla stopWords
def process(listOfOpinions, clusterNumber):
    # Prepare list of clusters
    listOfClusters = clusterCreator.tfidf_createClusters(listOfOpinions)
    chosen_cluster = listOfClusters[clusterNumber]
    # Tokenize chosen cluster
    cluster_tokenized = [word_tokenize(opinion) for opinion in chosen_cluster]
    # Create dictionary
    gensim_dictionary = Dictionary(cluster_tokenized)
    # Create corpus using tokenized cluster
    gensim_corpus = [gensim_dictionary.doc2bow(opinion) for opinion in cluster_tokenized]
    # Filter right created corpus from not significant words
    Utils().filterCorpus(gensim_corpus, gensim_dictionary, 0.03)
    # Create LdaModel
    lda_model = LdaModel(corpus=gensim_corpus, id2word=gensim_dictionary, num_topics=20)

    df = topicModelling.getTopicOpinionsDataFrame(chosen_cluster, gensim_corpus, lda_model)

    # Create df showing amout of opinions per topic
    df_count = df.groupby('Topic').size().reset_index(name='AmountOfOpinions')

    print(df_count)

    # Create and display topics plot
    topicModelling.displayTopicPlot(lda_model, gensim_corpus, gensim_dictionary)


process(opinionsPerAirline['wizz-air'], 2)

# process(listOfWholeOpinions)