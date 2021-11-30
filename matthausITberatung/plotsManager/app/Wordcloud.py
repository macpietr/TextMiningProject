from wordcloud import WordCloud
from matplotlib import pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()

UNION_STOP_WORDS = objectsManager.getSavedObject('unionStopWords')
mainOpinionsCorpus = objectsManager.getSavedObject('bigramsCorpus')


projectWordcloud = WordCloud(stopwords=UNION_STOP_WORDS, collocations=False, background_color="white", colormap="Dark2", max_font_size=150, random_state=42)

plt.rcParams['figure.figsize'] = [50,50]

for numberOfPlot, airline in enumerate(PathsManager().LIST_OF_AIRLINES):
    projectWordcloud.generate(mainOpinionsCorpus.opinions[airline])
    plt.subplot(3,4,numberOfPlot+1)
    plt.imshow(projectWordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(airline)

plt.show()