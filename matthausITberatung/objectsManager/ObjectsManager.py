import pandas

from matthausITberatung.objectsManager.PathsManager import PathsManager

class ObjectsManager:

    def saveObject(self, object, objectFileName):
        object.to_pickle(PathsManager().PICKLED_FILES() + "/" + objectFileName + ".pkl")

    def getSavedObject(self, objectFileName):
        return pandas.read_pickle(PathsManager().PICKLED_FILES() + "/" + objectFileName + ".pkl")
