import pandas as pd
import pyLDAvis.gensim
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk import word_tokenize
from sklearn.decomposition import LatentDirichletAllocation

from matthausITberatung.DataMining.LDA.Utils import Utils

class TopicModelling:
#TODO: zrobic dla bigrams i trigrams. dla kazdej linii lotniczej oraz dla wszystkich opinii

    def __tokenizeCluster(self, cluster):
        return [word_tokenize(opinion) for opinion in cluster]


    def displayTopicPlot(self, lda_model, corpus, dictionary):
        #PLOT
        pyLDAvis.enable_notebook()
        vis = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary, mds="mmds", R=30)
        pyLDAvis.show(vis)


    def getTopicOpinionsDataFrame(chosen_cluster, gensim_corpus, lda_model):
        # Assign opinion to topic
        opinion_topic_assignments = []
        for i, opinion in enumerate(chosen_cluster):
            # Assign topic using LDA model
            topic_assignment = max(lda_model[gensim_corpus[i]], key=lambda x: x[1])[0]

            opinion_topic_assignments.append((topic_assignment, opinion))
        # Create df from above list
        return pd.DataFrame(opinion_topic_assignments, columns=['Topic', 'Opinion'])