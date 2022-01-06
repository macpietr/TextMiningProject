from wordcloud import WordCloud
from matplotlib import pyplot as plt
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()
pathsManager = PathsManager()

UNION_STOP_WORDS = objectsManager.getSavedObject(pathsManager.UNION_STOP_WORDS)
dictOfCountersFromBigrams = objectsManager.getSavedObject(pathsManager.DICT_OF_COUNTERS_FROM_BIGRAMS)

for key in dictOfCountersFromBigrams.keys():
    print('########### '+key+' ##########')
    print(dictOfCountersFromBigrams[key].most_common(10))

    wordcloud = WordCloud(width = 1000, height = 500, background_color="white", stopwords=UNION_STOP_WORDS, colormap="Dark2")\
        .generate_from_frequencies(dictOfCountersFromBigrams[key])
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(key)
    plt.show()