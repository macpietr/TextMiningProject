import numpy
from matplotlib import pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

objectManager = ObjectsManager()

summaryTable = objectManager.getSavedObject('summaryTable')

y_pos = numpy.arange(len(summaryTable))

plt.subplot(1,3,1)
plt.title('Number of Unique Words', fontsize=10)
plt.bar(y_pos, summaryTable.unique_words, align='center')
plt.xticks(y_pos, summaryTable.airlines)

plt.subplot(1,3,2)
plt.title('Number of Total Words', fontsize=10)
plt.bar(y_pos, summaryTable.sum_of_words)
plt.xticks(y_pos, summaryTable.airlines)

plt.subplot(1,3,3)
plt.title('Avg. amount of Words per post', fontsize=10)
plt.bar(y_pos, summaryTable.sum_of_words_per_post)
plt.xticks(y_pos, summaryTable.airlines)

plt.tight_layout(pad=3)
plt.show()