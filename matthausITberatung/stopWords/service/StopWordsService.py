import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager


class StopWordsService:

    def __init__(self):
        nltk.download('stopwords')
        nltk.download('punkt')
        self.customStopWords = ObjectsManager().getSavedObject(PathsManager().UNION_STOP_WORDS)

    def remove_stopwords(self, data):
        stop_words = set(stopwords.words('english')).union(self.customStopWords)

        tokens = word_tokenize(data)
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
        filtered_text = ' '.join(filtered_tokens)

        return filtered_text