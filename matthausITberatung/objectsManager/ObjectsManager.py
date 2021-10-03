import pandas

from matthausITberatung.objectsManager.PathsManager import PathsManager

class ObjectsManager:

    def saveObject(self, object):
        object.to_pickle(PathsManager().PICKLED_FILES() + "/" + object + ".pkl")

    def getSavedObject(self, object):
        return pandas.read_pickle(PathsManager().PICKLED_FILES() + "/" + object + ".pkl")
