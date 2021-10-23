from matthausITberatung.dataCleaner.cleaner.DataCleaner import DataCleaner


dataCleaner = DataCleaner()
nameOfDataChildDirsList = ['TitleOfOpinion','MainUserOpinion','MainMarkInOpinion']

for nameOfDataChildDir in nameOfDataChildDirsList:
    dataCleaner.cleanAndWriteData(nameOfDataChildDir)