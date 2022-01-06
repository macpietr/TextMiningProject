from wordcloud import WordCloud
from matplotlib import pyplot as plt
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

objectsManager = ObjectsManager()

UNION_STOP_WORDS = objectsManager.getSavedObject('unionStopWords')
mainOpinionsCorpus = objectsManager.getSavedObject('bigramsCorpus')

dictOfCountersFromBigrams = objectsManager.getSavedObject('dictOfCountersFromBigrams')

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