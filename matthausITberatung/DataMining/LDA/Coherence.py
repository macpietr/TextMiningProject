# from gensim.models import CoherenceModel
# from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
#
# objectsManager = ObjectsManager()
#
# topicModelling = objectsManager.getSavedObject('topicModelling_lufthansa_0')
#
# coherence_model_lda = CoherenceModel(model=topicModelling.lda_model, texts=topicModelling.cluster_tokenized, dictionary=topicModelling.gensim_dictionary, coherence='c_v')
# if __name__ == '__main__':
#     coherence_lda = coherence_model_lda.get_coherence()
#     print('\nCoherence Score: ', coherence_lda)
from gensim.models import LdaModel, CoherenceModel
from matthausITberatung.DataMining.LDA.TopicModelling import TopicModelling
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

pathsManager = PathsManager()
objectsManager = ObjectsManager()

topicModelling = TopicModelling(pathsManager.WIZZ_AIR, 2, 10)


# def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
#     coherence_values = []
#     model_list = []
#     for num_topics in range(start, limit, step):
#         lda_model = LdaModel(corpus=corpus,
#                                   id2word=dictionary,
#                                   num_topics=num_topics,
#                                   chunksize=len(topicModelling.chosen_cluster),
#                                   passes=20,
#                                   random_state=100)
#         model_list.append(lda_model)
#         coherence_model_lda = CoherenceModel(model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v')
#         if __name__ == '__main__':
#             coherence_values.append(coherence_model_lda.get_coherence())
#
#     return model_list, coherence_values
#
# model_list, coherence_values = compute_coherence_values(dictionary=topicModelling.gensim_dictionary,
#                                                         corpus=topicModelling.gensim_corpus,
#                                                         texts=topicModelling.cluster_tokenized,
#                                                         start=2, limit=40, step=6)

# objectsManager.saveObject(model_list,'model_list')
# objectsManager.saveObject(coherence_values,'coherence_values')


coherence_values = []
for i in range(1,16):
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

# coherence_values = objectsManager.getSavedObject('coherence_values_lufthansa_1')
#
# limit=16; start=1; step=1;
# x = range(start, limit, step)
# plt.plot(x, coherence_values)
# plt.title("Lufthansa Cluster_1 Coherence plot")
# plt.xlabel("Num Topics")
# plt.ylabel("Coherence score")
# plt.legend(("coherence_values"), loc='best')
# plt.show()