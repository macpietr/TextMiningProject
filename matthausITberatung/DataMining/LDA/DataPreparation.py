from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner
from matthausITberatung.objectsManager.FileReader import FileReader
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.stopWords.service.StopWordsService import StopWordsService

stopWordsService = StopWordsService()

def __lemmatizeAirLineOpinions(airlineOpinions):
    perAirlineList = []
    for opinion in airlineOpinions:
        helperString = DataCleaner().lemmatizeLine(opinion)
        perAirlineList.append(helperString)
    return perAirlineList

def prepareData():
    # custom_stop_words = list(ObjectsManager().getSavedObject('STOP_WORDS_LIST_FROM_SHORT_WORDS'))
    listOfWholeOpinions = []
    opinionsPerAirline = {}
    for airline in PathsManager().LIST_OF_AIRLINES:
        airlineOpinions = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR, 'MainUserOpinion', airline) \
            .split('\n')
        lemmatizedOpinions = __lemmatizeAirLineOpinions(airlineOpinions)
        lemmatizedOpinions_withoutStopWords = stopWordsService.remove_stopwords(lemmatizedOpinions)
        opinionsPerAirline[airline] = lemmatizedOpinions_withoutStopWords
        listOfWholeOpinions.append(lemmatizedOpinions_withoutStopWords)
    ObjectsManager().saveObject(listOfWholeOpinions, 'listOfWholeOpinions')
    ObjectsManager().saveObject(opinionsPerAirline, 'opinionsPerAirline')

prepareData()

print("Data Preparation is finished")