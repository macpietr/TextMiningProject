from gensim.models import LdaModel, CoherenceModel
from matthausITberatung.DataMining.LDA.TopicModelling import TopicModelling
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

pathsManager = PathsManager()
objectsManager = ObjectsManager()

topicModelling = TopicModelling(pathsManager.WIZZ_AIR, 2, 10)

coherence_values = []
for i in range(1,11):
    lda_model = LdaModel(corpus=topicModelling.gensim_corpus,
                         id2word=topicModelling.gensim_dictionary,
                         num_topics=i,
                         chunksize=len(topicModelling.chosen_cluster),
                         passes=20,
                         random_state=100)

    coherence_model_lda = CoherenceModel(model=lda_model, texts=topicModelling.cluster_tokenized,
                                         dictionary=topicModelling.gensim_dictionary, coherence='c_v')
    if __name__ == '__main__':
        result = coherence_model_lda.get_coherence()
        print(result)
        coherence_values.append(result)

objectsManager.saveObject(coherence_values, 'coherence_values_ryanair_1')