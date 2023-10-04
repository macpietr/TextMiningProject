import pandas as pd

from matthausITberatung.DataMining.LDA.TopicModelling import TopicModelling
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

objectsManager = ObjectsManager()

opinionsPerAirline = objectsManager.getSavedObject('opinionsPerAirline')
listOfWholeOpinions = objectsManager.getSavedObject('listOfWholeOpinions')

#(listOfOpinions, clusterNumber)
topicModelling = TopicModelling(opinionsPerAirline['ryanair'], 2)

def process(topicModelling):
    # Prepare list of clusters
    df_topic_opinion = topicModelling.getTopicOpinionsDataFrame()
    print(df_topic_opinion)
    # Create df showing amount of opinions per topic
    df_count_topic_opinion = df_topic_opinion.groupby(['TopicId', 'TopicWords']).size().reset_index(name='AmountOfOpinions')
    print(df_count_topic_opinion)

    # Create and display topics plot
    topicModelling.displayTopicPlot()

    # print(topicModelling.getMainDf())

    # print(topicModelling.createMainDf())


process(topicModelling)

# process(listOfWholeOpinions)