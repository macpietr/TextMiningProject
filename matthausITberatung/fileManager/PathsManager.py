class PathsManager:

    def WIZZ_AIR(self):
        return 'wizz-air'

    def RYANAIR(self):
        return 'ryanair'

    def LUFTHANSA(self):
        return 'lufthansa'

    def LIST_OF_AIRLINES(self):
        return [self.LUFTHANSA(),self.RYANAIR(),self.WIZZ_AIR()]

    def PROJECT_ROOT_DIR(self):
        path = 'C:\\Users\\macie\\Documents\\TextMiningProject\\matthausITberatung\\output_files\\'
        return path

    def DOWNLOADED_FILES_DIR(self):
        path = self.PROJECT_ROOT_DIR() + 'downloaded_files'
        return path

    def CLEANED_DATA_FILES_DIR(self):
        path = self.PROJECT_ROOT_DIR() + 'cleaned_data_files'
        return path