from matthausITberatung.DataMining.LDA.TopicModelling import TopicModelling
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

listOfClusters_wholeOpinions = ObjectsManager().getSavedObject('listOfClusters_wholeOpinions')

dictOfAirlinesClusters = ObjectsManager().getSavedObject('dictOfAirlinesClusters')

TopicModelling().displayTopicPlot(dictOfAirlinesClusters['wizz-air'][2])