from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.topicModelling.tfidf.TfidfUtils import TfidfUtils

commondatavectors = ObjectsManager().getSavedObject('commondatavectors')
lufthansavectors = ObjectsManager().getSavedObject('lufthansavectors')
ryanairvectors = ObjectsManager().getSavedObject('ryanairvectors')
wizzairvectors = ObjectsManager().getSavedObject('wizz-airvectors')

TfidfUtils().showExpectedClustersPlot(commondatavectors, 'Whole opinions clusters no. plot')
TfidfUtils().showExpectedClustersPlot(lufthansavectors, 'Lufthansa clusters no. plot')
TfidfUtils().showExpectedClustersPlot(ryanairvectors, 'Ryanair clusters no. plot')
TfidfUtils().showExpectedClustersPlot(wizzairvectors, 'Wizz-air clusters no. plot')
