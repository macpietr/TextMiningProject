print('run all modules')
print('###############')
print('run data downloader module')
from matthausITberatung.dataDownloader.app import Main
print('Run dataCleaner module')
from matthausITberatung.dataCleaner.app import Main
print('Run stopWords module')
from matthausITberatung.stopWords.app import Main
print('Run exploratoryDataAnalyser')
from matthausITberatung.exploratoryDataAnalyser.app import Main
print('All modules were executed')