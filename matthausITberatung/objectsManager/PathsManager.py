class PathsManager:

    WIZZ_AIR = 'wizz-air'

    RYANAIR = 'ryanair'

    LUFTHANSA = 'lufthansa'

    LIST_OF_AIRLINES = [LUFTHANSA,RYANAIR,WIZZ_AIR]

    PROJECT_ROOT_DIR = 'C:\\Users\\macie\\Documents\\TextMiningProject\\matthausITberatung\\output_files\\'

    DOWNLOADED_FILES_DIR = PROJECT_ROOT_DIR + 'downloaded_files'

    CLEANED_DATA_FILES_DIR = PROJECT_ROOT_DIR + 'cleaned_data_files'

    def PICKLED_FILES(self):
        path = self.PROJECT_ROOT_DIR() + 'pickled_files'
        return path