from collections import Counter

from wordcloud import WordCloud
from matplotlib import pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()
pathsManager = PathsManager()

# dictOfListOf30CountedMostCommonWords = objectsManager.getSavedObject(pathsManager.DICT_OF_LIST_OF_30_COUNTED_MOST_COMMON_WORDS)
# dictOfListOf30CountedMostCommonBigrams = objectsManager.getSavedObject(pathsManager.DICT_OF_LIST_OF_30_COUNTED_MOST_COMMON_BIGRAMS)

dictOfDictsOfAirlinesClustersOpinions = objectsManager.getSavedObject('dictOfDictsOfAirlinesClustersOpinions')

# for airline in pathsManager.LIST_OF_AIRLINES:
#     print('########### '+airline+' ##########')
#
#     wordcloud = WordCloud(width = 1000, height = 500, background_color="white",
#                           stopwords=objectsManager.getSavedObject(pathsManager.UNION_STOP_WORDS), colormap="Dark2")\
#         .generate_from_frequencies(dictOfListOf30CountedMostCommonBigrams[airline])
#     plt.figure(figsize=(15,8))
#     plt.imshow(wordcloud, interpolation="bilinear")
#     plt.axis("off")
#     plt.title(airline, fontsize=30)
#     plt.show()

def generate_wordcloud(data, title, position):
    wordcloud = WordCloud(width=600, height=300, colormap="Dark2", background_color='white').generate(' '.join(data))
    plt.subplot(3, 3, position)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)

plt.figure(figsize=(15, 8))

position = 1
for key, subDict in dictOfDictsOfAirlinesClustersOpinions.items():
    for subKey, opinion in subDict.items():
        generate_wordcloud(opinion, str(key)+' - Cluster_'+str(int(subKey+1)), position)
        position += 1

plt.tight_layout()
plt.show()