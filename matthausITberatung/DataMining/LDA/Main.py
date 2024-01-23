from matthausITberatung.DataMining.LDA.TopicModelling import TopicModelling
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()

pathsManager = PathsManager()

#(listOfOpinions, clusterNumber, numberOfTopics)
# topicModelling = TopicModelling(opinionsPerAirline['ryanair'], 2)
topicModelling = TopicModelling(pathsManager.WIZZ_AIR, 2, 3)

def labeling(topicModelling):
    topic_labels = []
    for doc in topicModelling.gensim_corpus:
        dominant_topic = max(topicModelling.lda_model[doc], key=lambda x: x[1])
        topic_labels.append(dominant_topic[0])
    print(topic_labels)



def process(topicModelling):
    # Prepare list of clusters
    df_topic_opinion = topicModelling.getTopicOpinionsDataFrame()
    print(df_topic_opinion)
    # Create df showing amount of opinions per topic
    df_count_topic_opinion = df_topic_opinion.groupby(['TopicId']).size().reset_index(name='AmountOfOpinions')
    objectsManager.saveObject(df_topic_opinion, 'df_topic_opinion_'+topicModelling.airline+'_'+str(topicModelling.clusterNumber))
    objectsManager.saveObject(df_count_topic_opinion, 'df_count_topic_opinion_'+topicModelling.airline+'_'+str(topicModelling.clusterNumber))
    objectsManager.saveObject(topicModelling, 'topicModelling_'+topicModelling.airline+'_'+str(topicModelling.clusterNumber))
    print(df_count_topic_opinion)

    # Create and display topics plot
    topicModelling.print_topics()
    # topicModelling.displayTopicPlot()
    # coherence_model_lda = CoherenceModel(model=topicModelling.lda_model, texts=topicModelling.cluster_tokenized,
    #                                      dictionary=topicModelling.gensim_dictionary, coherence='c_v')
    # if __name__ == '__main__':
    #     coherence_lda = coherence_model_lda.get_coherence()
    #     print('Coherence')
    #     print(coherence_lda)

    # print(topicModelling.getMainDf())

    # print(topicModelling.createMainDf())


process(topicModelling)

# process(listOfWholeOpinions)