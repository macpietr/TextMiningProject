import pandas as pd
import pyLDAvis.gensim
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk import word_tokenize
from sklearn.decomposition import LatentDirichletAllocation

from matthausITberatung.DataMining.LDA.Utils import Utils
from matthausITberatung.DataMining.tfidf.clustering.ClusterCreator import ClusterCreator


class TopicModelling:
#TODO: zrobic dla bigrams i trigrams. dla kazdej linii lotniczej oraz dla wszystkich opinii

    def __init__(self, listOfOpinions, clusterNumber):
        self.clusterCreator = ClusterCreator()
        self.listOfClusters = self.clusterCreator.tfidf_createClusters(listOfOpinions)
        self.chosen_cluster = self.listOfClusters[clusterNumber]
        # Tokenize chosen cluster
        self.cluster_tokenized = [word_tokenize(opinion) for opinion in self.chosen_cluster]
        # Create dictionary
        self.gensim_dictionary = Dictionary(self.cluster_tokenized)
        # Create corpus using tokenized cluster
        self.gensim_corpus = [self.gensim_dictionary.doc2bow(opinion) for opinion in self.cluster_tokenized]
        Utils().filterCorpus(self.gensim_corpus, self.gensim_dictionary, 0.03)
        # Create LdaModel
        self.lda_model = LdaModel(corpus=self.gensim_corpus, id2word=self.gensim_dictionary, num_topics=20)

    def displayTopicPlot(self):
        #PLOT
        pyLDAvis.enable_notebook()
        vis = pyLDAvis.gensim.prepare(self.lda_model, self.gensim_corpus, self.gensim_dictionary, mds="mmds", R=30)
        pyLDAvis.show(vis)

    def getTopicOpinionsDataFrame(self):
        # Assign opinion to topic
        opinion_topic_assignments = []
        for i, opinion in enumerate(self.chosen_cluster):
            # Assign topic using LDA model
            topic_assignment = max(self.lda_model[self.gensim_corpus[i]], key=lambda x: x[1])[0]
            topic_words = ", ".join([word for word, _ in self.lda_model.show_topic(topic_assignment)])
            opinion_topic_assignments.append((topic_assignment, topic_words, opinion))

        # Create df from above list
        return pd.DataFrame(opinion_topic_assignments, columns=['TopicId', 'TopicWords', 'Opinion'])

    # def __getTopicOpinionsDataFrame(self):
    #     # Assign opinion to topic
    #     opinion_topic_assignments = []
    #     for i, opinion in enumerate(self.chosen_cluster):
    #         # Assign topic using LDA model
    #         topic_assignment = max(self.lda_model[self.gensim_corpus[i]], key=lambda x: x[1])[0]
    #
    #
    #         opinion_topic_assignments.append((topic_assignment, opinion))
    #     # Create df from above list
    #     return pd.DataFrame(opinion_topic_assignments, columns=['Topic', 'Opinion'])

    def __tokenizeCluster(self, cluster):
        return [word_tokenize(opinion) for opinion in cluster]