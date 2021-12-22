from collections import Counter

from wordcloud import WordCloud
from matplotlib import pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()

UNION_STOP_WORDS = objectsManager.getSavedObject('unionStopWords')
mainOpinionsCorpus = objectsManager.getSavedObject('bigramsCorpus')

# dictOfListsOfBigrams = objectsManager.getSavedObject('dictOfListsOfBigrams')
dictOfCountersFromBigrams = objectsManager.getSavedObject('dictOfCountersFromBigrams')

# lufthansaClearedList = [term for term in dictOfCounters['lufthansa'] if ]

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


# projectWordcloud = WordCloud(stopwords=UNION_STOP_WORDS, collocations=False, background_color="white", colormap="Dark2", max_font_size=150, random_state=42)
#
# plt.rcParams['figure.figsize'] = [50,50]
#
# for numberOfPlot, airline in enumerate(PathsManager().LIST_OF_AIRLINES):
#     projectWordcloud.generate(dictOfListsOfBigrams[airline])
#     plt.subplot(3,4,numberOfPlot+1)
#     plt.imshow(projectWordcloud, interpolation="bilinear")
#     plt.axis("off")
#     plt.title(airline)
#
# plt.show()