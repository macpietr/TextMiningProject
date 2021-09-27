from matthausITberatung.dataCleaner.cleaner.MainUserOpinionCleaner import MainUserOpinionCleaner
from matthausITberatung.fileManager.FileReader import FileReader
from matthausITberatung.fileManager.FileWriter import FileWriter
from matthausITberatung.fileManager.PathsManager import PathsManager
import pandas as pd

# for airline in PathsManager().LIST_OF_AIRLINES():
#     data = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR(),'MainUserOpinion',airline)
#     cleanedData = MainUserOpinionCleaner(data).cleanData()
#     FileWriter(airline, 'MainUserOpinionFullCleand', PathsManager().CLEANED_DATA_FILES_DIR()).putDataIntoFile(cleanedData)


cleanedDataMap = {}
for i, airline in enumerate(PathsManager().LIST_OF_AIRLINES()):
    downloadedData = FileReader().readFile(PathsManager().CLEANED_DATA_FILES_DIR(),'MainUserOpinion',airline)
    cleanedDataMap[airline] = MainUserOpinionCleaner().cleanData(downloadedData)

print(cleanedDataMap.keys())

#nie wiem do czego to ale chyba potrzebne - nie wiem czym się różni mapa poniżej od mapy powyżej
prepareDataForCorpus = {key: [cleanedDataMap[key]] for (key,value) in cleanedDataMap.items()}

pd.set_option('max_colwidth',200)

corpus = pd.DataFrame.from_dict(prepareDataForCorpus).transpose()
corpus.columns = ['opinions']
corpus = corpus.sort_index()

print(corpus)

# print(corpus.opinions.loc[PathsManager().LUFTHANSA()])
