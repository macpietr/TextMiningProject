from matthausITberatung.DataMining.LDA.TopicModelling import TopicModelling
from matthausITberatung.DataMining.tfidf.clustering.ClusterCreator import ClusterCreator
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

#wyczyścić to ze stopWordsow
opinionsPerAirline = ObjectsManager().getSavedObject('opinionsPerAirline')


#TODO: cos znowu jest nie tak ze stopWordsami - temu powinienem się dobrze przyjrzeć i stworzyć zbiór ostateczny dla stopWords
def process(listOfOpinions, clusterNumber):
    listOfClusters = ClusterCreator().tfidf_createClusters(listOfOpinions)
    TopicModelling().displayTopicPlot(listOfClusters[clusterNumber])


process(opinionsPerAirline['wizz-air'], 2)