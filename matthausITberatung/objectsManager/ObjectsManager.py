import pickle

import pandas

from matthausITberatung.objectsManager.PathsManager import PathsManager

class ObjectsManager:

    def saveObject(self, object, objectFileName):
        with open(PathsManager().PICKLED_FILES() + "/" + objectFileName + ".pkl", 'wb') as pickledFile:
            pickle.dump(object, pickledFile)

    def getSavedObject(self, objectFileName):
        with open(PathsManager().PICKLED_FILES() + "/" + objectFileName + ".pkl", 'rb') as pickledFile:
            return pickle.load(pickledFile)
