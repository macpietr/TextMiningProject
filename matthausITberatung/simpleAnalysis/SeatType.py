import pandas
import pandas as pd

from matthausITberatung.objectsManager.PathsManager import PathsManager
from matthausITberatung.exploratoryDataAnalyser.analyser.DataDictManager import DataDictManager

pathsManager = PathsManager()
dataDictManager = DataDictManager()
airlines = pathsManager.LIST_OF_AIRLINES

dictOfSeatTypeStrings = dataDictManager.getDataDictFromFiles(pathsManager.DOWNLOADED_FILES_DIR, 'SeatType')

dictOfSeatTypeLists = {}
for airline in airlines:
    dictOfSeatTypeLists[airline] = dictOfSeatTypeStrings[airline].split('\n')
    dictOfSeatTypeLists[airline]

dictOfCounts = {}
for airline in airlines:
    dictOfCounts[airline] = pandas.value_counts(dictOfSeatTypeLists[airline])

for airline in airlines:
    allCount = sum(dictOfCounts[airline])
    df = pd.DataFrame.from_dict(dictOfCounts[airline])
    df.columns = ['count']
    percentage = [str(round((count/allCount)*100,3)) +'%' for count in dictOfCounts[airline]]
    df.insert(1, "percentage", percentage, True)

    print(airline)
    print(df)
    print('#######################################################')