from collections import Counter

from wordcloud import WordCloud
from matplotlib import pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()
pathsManager = PathsManager()

UNION_STOP_WORDS = objectsManager.getSavedObject(pathsManager.UNION_STOP_WORDS)
dataDictWithoutStopWords = objectsManager.getSavedObject(pathsManager.DATA_DICT_WITHOUT_STOP_WORDS)

dataDictOfListsOfWordsWithoutStopWords = {}
for key in dataDictWithoutStopWords.keys():
    dataDictOfListsOfWordsWithoutStopWords[key] = dataDictWithoutStopWords[key].split(" ")

dictOfCounters = {}
for key in dataDictWithoutStopWords.keys():
    dictOfCounters[key] = Counter(dataDictOfListsOfWordsWithoutStopWords[key])
# projectWordcloud = WordCloud(stopwords=UNION_STOP_WORDS, collocations=False,
#                              background_color="white", colormap="Dark2", max_font_size=150, random_state=42)
#
# plt.rcParams['figure.figsize'] = [50,50]

for key in dictOfCounters.keys():
    print('########### '+key+' ##########')
    print(dictOfCounters[key].most_common(10))

    wordcloud = WordCloud(width = 1000, height = 500, background_color="white", stopwords=UNION_STOP_WORDS, colormap="Dark2")\
        .generate_from_frequencies(dictOfCounters[key])
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(key)
    plt.show()