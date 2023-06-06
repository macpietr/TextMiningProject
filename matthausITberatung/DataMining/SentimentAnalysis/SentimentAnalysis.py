from textblob import TextBlob

from matthausITberatung.DataMining.LDA.TopicModelling import TopicModelling
from matthausITberatung.DataMining.tfidf.clustering.ClusterCreator import ClusterCreator
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

objectsManager = ObjectsManager()
clusterCreator = ClusterCreator()

opinionsPerAirline = objectsManager.getSavedObject('opinionsPerAirline')

topicModelling = TopicModelling(opinionsPerAirline['wizz-air'], 2)

df_topic_opinion = topicModelling.getTopicOpinionsDataFrame()

# # todo: sprawdzić co jest tutaj nie tak. czy wydzielac opinie per topic i dopiero liczyc polarity czy robic to w locie?
# # todo: ?? df_topic_opinion_grouped = df_topic_opinion.groupby('Topic')['Opinion'].apply(lambda x: TextBlob(' '.join(x)).polarity).reset_index()
#
# # df_topic_opinion_grouped = df_topic_opinion.groupby(['Topic ID', 'Topic Words'])['Opinion'].apply(lambda x: ' '.join(x)).reset_index()
#
# # df_topic_polarity = df_topic_opinion_grouped['Opinion'].apply(lambda x: TextBlob(x).polarity)
#
# df_topic_opinion_grouped = df_topic_opinion.groupby('Topic ID')['Opinion'].apply(lambda x: TextBlob(' '.join(x)).polarity).reset_index()
#
# print(df_topic_opinion_grouped)

# print(df_topic_polarity)

#TODO: wyświetlić wyrazy dla topiców zamiast numerów




# TODO: może po kolei, żeby nikt dwa razy wpier***u nie dostał

# TODO: zacznijmy od dataframe opinie i polarity

df_topic_opinion = topicModelling.getTopicOpinionsDataFrame()

df_topic_opinion_opinionPolarity = df_topic_opinion.assign(OpinionPolarity = df_topic_opinion['Opinion'].apply(lambda x: TextBlob(x).polarity))

print(df_topic_opinion_opinionPolarity)

# df = pd.DataFrame(columns=["Opinion", "Polarity"])
#
# listOfClusters = clusterCreator.tfidf_createClusters(listOfOpinions)
# # chosen_cluster = listOfClusters[clusterNumber]
#
# cluster_polarity_dict = {}
# clusterNumber = 0
# for cluster in listOfClusters:
#     cluster_polarity_dict[clusterNumber] = TextBlob(str(' '.join(cluster))).polarity
#     clusterNumber = clusterNumber + 1
#
#
#
#
# # for opinion in listOfOpinions:
# #     df = df.append({"Opinion": opinion, "Polarity": TextBlob(opinion).polarity}, ignore_index=True)
#
#
#
# print(cluster_polarity_dict)
#
# # polarity_sum = df["Polarity"].sum()
# #
# # print(polarity_sum/1200)
# #
# # print(TextBlob(' '.join(opinionsPerAirline['ryanair'])).polarity)