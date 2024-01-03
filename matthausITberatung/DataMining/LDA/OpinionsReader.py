from gensim.models import CoherenceModel

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()
pathsManager = PathsManager()

airline = pathsManager.LUFTHANSA
clusterNumber = 1

df_cluster = objectsManager.getSavedObject('df_topic_opinion_'+pathsManager.LUFTHANSA+'_'+str(clusterNumber))

def listOfOpinionsPerTopic(topicNumber):
    return df_cluster[df_cluster.apply(lambda row: row['TopicId'] == topicNumber, axis=1)]['Opinion'].tolist()

# [print(item) for item in listOfOpinionsPerTopic(2)]
# print(df_cluster[df_cluster.apply(lambda row: row['TopicId'] == 1, axis=1)])

topic_proportion = df_cluster.groupby('Opinion').filter(lambda x: x['TopicId'].nunique() > 0)[['Opinion', 'Adjustment','TopicId']]
topic_assignment = df_cluster.groupby('TopicId').filter(lambda x: x['Opinion'].nunique() > 0)[['TopicId', 'Adjustment','Opinion']].sort_values(by='TopicId')

df_filtered = df_cluster[df_cluster['Opinion'].str.strip() != '']

# print(df_filtered[df_filtered.apply(lambda row: row['TopicId'] == 1, axis=1)])

topicModelling = objectsManager.getSavedObject('topicModelling_lufthansa_0')

coherence_model_lda = CoherenceModel(model=topicModelling.lda_model, texts=topicModelling.cluster_tokenized, dictionary=topicModelling.gensim_dictionary, coherence='c_v')
if __name__ == '__main__':
    coherence_lda = coherence_model_lda.get_coherence()
    print('\nCoherence Score: ', coherence_lda)