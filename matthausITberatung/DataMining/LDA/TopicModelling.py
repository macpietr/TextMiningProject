from pprint import pprint

import pandas as pd
import pyLDAvis.gensim
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk import word_tokenize
from matthausITberatung.DataMining.LDA.Utils import Utils
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager


class TopicModelling:

    def __init__(self, airline, clusterNumber, numberOfTopics):
        self.airline = airline
        self.clusterNumber = clusterNumber
        self.dictOfDictsOfAirlinesClustersOpinions = ObjectsManager().getSavedObject('dictOfDictsOfAirlinesClustersOpinions')
        self.listOfOpinions = self.dictOfDictsOfAirlinesClustersOpinions[airline][clusterNumber]
        self.chosen_cluster = self.listOfOpinions
        # Tokenize chosen cluster
        self.cluster_tokenized = [word_tokenize(opinion) for opinion in self.chosen_cluster]
        # Create dictionary
        self.gensim_dictionary = Dictionary(self.cluster_tokenized)
        # Create corpus using tokenized cluster
        self.gensim_corpus = [self.gensim_dictionary.doc2bow(opinion) for opinion in self.cluster_tokenized]
        Utils().filterCorpus(self.gensim_corpus, self.gensim_dictionary, 0.03)
        # Create LdaModel
        self.lda_model = LdaModel(corpus=self.gensim_corpus,
                                  id2word=self.gensim_dictionary,
                                  num_topics=numberOfTopics,
                                  chunksize=len(self.chosen_cluster),
                                  passes=20,
                                  random_state=100)


    def displayTopicPlot(self):
        #PLOT
        pyLDAvis.enable_notebook()
        vis = pyLDAvis.gensim.prepare(self.lda_model, self.gensim_corpus, self.gensim_dictionary, mds="mmds", R=30)
        pyLDAvis.show(vis)

    def print_topics(self):

        output_lda = self.lda_model.print_topics(num_words=30)

        excel_path = 'C:\\Users\\macie\\Downloads\\lda_topics.xlsx'  # Ścieżka do zapisania pliku Excel
        with pd.ExcelWriter(excel_path) as writer:
            for topic_num, words in output_lda:
                data = []
                for word_info in words.split(' + '):
                    proportion, word = word_info.split('*')
                    word = word.strip('"')
                    data.append((word, float(proportion)))
                topic_df = pd.DataFrame(data, columns=['word', 'word_proportion'])
                topic_df.to_excel(writer, sheet_name=f'Topic_{topic_num}', index=False)

        excel_path

    # a measure of how good the model is. lower the better.
    def showPerplexity(self):
        print('Perplexity')
        print(self.lda_model.log_perplexity(self.gensim_corpus))

    def getTopicOpinionsDataFrame(self):
        document_topics = [self.lda_model.get_document_topics(doc) for doc in self.gensim_corpus]
        data = {'TopicId': [], 'Adjustment': [], 'Opinion': []}
        for i, topics in enumerate(document_topics):
            for topic in topics:
                data['TopicId'].append(topic[0]+1)
                data['Adjustment'].append(topic[1])
                data['Opinion'].append(self.listOfOpinions[i])

        return pd.DataFrame(data)