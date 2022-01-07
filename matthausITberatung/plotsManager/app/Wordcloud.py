from collections import Counter

from wordcloud import WordCloud
from matplotlib import pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()
pathsManager = PathsManager()

UNION_STOP_WORDS = objectsManager.getSavedObject(pathsManager.UNION_STOP_WORDS)
airlinesDictOfCountedWordsCounter = objectsManager.getSavedObject(pathsManager.AIRLINES_DICT_OF_COUNTED_WORDS_COUNTER)

for key in airlinesDictOfCountedWordsCounter.keys():
    print('########### '+key+' ##########')
    print(airlinesDictOfCountedWordsCounter[key].most_common(10))

    wordcloud = WordCloud(width = 1000, height = 500, background_color="white", stopwords=UNION_STOP_WORDS, colormap="Dark2")\
        .generate_from_frequencies(airlinesDictOfCountedWordsCounter[key])
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(key)
    plt.show()