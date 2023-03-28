import statistics
import pandas
from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.exploratoryDataAnalyser.analyser.CorpusManager import CorpusManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataTermMatrixManager import DataTermMatrixManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager
from matthausITberatung.simpleAnalysis.helper.Helper import Helper

pathsManager = PathsManager()
dataDictManager = DataDictManager()
dataCleaner = DataCleaner()
helper = Helper()
corpusManager = CorpusManager()
dtmManager = DataTermMatrixManager()
airlines = pathsManager.LIST_OF_AIRLINES

numberAnalysisDirectories = pathsManager.NUMBER_ANALYSIS_DIRS

numberAnalysisDictOfStrings = {}
for directory in numberAnalysisDirectories:
    numberAnalysisDictOfStrings[directory] = dataDictManager.getDataDictFromFiles(pathsManager.DOWNLOADED_FILES_DIR, directory)

#Had to add it separately, because it needed deepen cleaning
numberAnalysisDictOfStrings['MainMarkInOpinion'] = dataDictManager.getDataDictFromFiles(pathsManager.CLEANED_DATA_FILES_DIR, 'MainMarkInOpinion')

print(numberAnalysisDictOfStrings)

clearedNumberAnalysisDictOfStrings = {}
for directory in numberAnalysisDictOfStrings.keys():
    clearedNumberAnalysisDictOfStrings[directory] = dataCleaner.cleanDataForNumberAnalysis(numberAnalysisDictOfStrings[directory])

print(clearedNumberAnalysisDictOfStrings)

numberAnalysisDictOfLists = {}
for directory in numberAnalysisDictOfStrings.keys():
    numberAnalysisDictOfLists[directory] = helper.createDictOfLists(clearedNumberAnalysisDictOfStrings[directory])

print(numberAnalysisDictOfLists)

numberAnalysisDictOfListsOfInts = {}
for directory in numberAnalysisDictOfStrings.keys():
    numberAnalysisDictOfListsOfInts[directory] = helper.convertStringsToInts(numberAnalysisDictOfLists[directory])

print(numberAnalysisDictOfListsOfInts)

print(statistics.mode(numberAnalysisDictOfListsOfInts['GroundService']['wizz-air']))

numberAnalysisDictOfDataFrames = {}
for directory in numberAnalysisDictOfStrings.keys():
    listOfModes = [statistics.mode(numberAnalysisDictOfListsOfInts[directory][airline]) for airline in pathsManager.LIST_OF_AIRLINES]
    listOfMedians = [statistics.median(numberAnalysisDictOfListsOfInts[directory][airline]) for airline in pathsManager.LIST_OF_AIRLINES]
    listOfMeans = [round(statistics.mean(numberAnalysisDictOfListsOfInts[directory][airline]),2) for airline in pathsManager.LIST_OF_AIRLINES]
    listOfStdevs = [round(statistics.stdev(numberAnalysisDictOfListsOfInts[directory][airline]),2) for airline in pathsManager.LIST_OF_AIRLINES]
    listOfCounts = [len(numberAnalysisDictOfListsOfInts[directory][airline]) for airline in pathsManager.LIST_OF_AIRLINES]
    data = {'mode':listOfModes,
            'median':listOfMedians,
            'mean':listOfMeans,
            'stdev':listOfStdevs,
            'counts':listOfCounts}
    numberAnalysisDictOfDataFrames[directory] = pandas.DataFrame(data, index=pathsManager.LIST_OF_AIRLINES)
    print(directory)
    print(numberAnalysisDictOfDataFrames[directory])
