import numpy
from matplotlib import pyplot as plt
from textblob import TextBlob

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

# objectManager = ObjectsManager()
# pathsManager = PathsManager()
#
# summaryTable = objectManager.getSavedObject(pathsManager.SUMMARY_TABLE)
#
# y_pos = numpy.arange(len(summaryTable))
#
# plt.subplot(1,3,1)
# plt.title('Number of Unique Words', fontsize=10)
# plt.bar(y_pos, summaryTable.unique_words, align='center')
# plt.xticks(y_pos, summaryTable.airlines, rotation=55)
#
# plt.subplot(1,3,2)
# plt.title('Number of Total Words', fontsize=10)
# plt.bar(y_pos, summaryTable.sum_of_words)
# plt.xticks(y_pos, summaryTable.airlines, rotation=55)
#
# plt.subplot(1,3,3)
# plt.title('Avg. amount of Words per post', fontsize=10)
# plt.bar(y_pos, summaryTable.avg_amount_of_words_per_post)
# plt.xticks(y_pos, summaryTable.airlines, rotation=55)
#
# plt.tight_layout(pad=3)
# plt.show()

dictOfDictsOfAirlinesClustersOpinions = ObjectsManager().getSavedObject('dictOfDictsOfAirlinesClustersOpinions')
opinion = dictOfDictsOfAirlinesClustersOpinions['lufthansa'][0][0]
# opinion = 'Flight was delayed from LHR. No information for connecting flight at Munich airport. 1 hour transit time reduced to 30 minutes - horrible airport experience with no Guidance at Munich. They lost my bag which was did not arrive on 16th Dec in Oman. Day 18 of Lost Bag on 01st Jan 2023.  I bought the ticket from their website no discount or changes from my end. Please avoid this airline and MUC airport. 18 days and my bag with family gifts for Xmas and other essentials is nowhere in site. LH tells me to ask the connecting flight operator Oman air, but my bag is in LH custody which they have not released to Oman Air! LH ground staff at LHR needs more training as well. A learning experience for me.'
# opinion = 'flight was delayed from lhr no information for connecting flight at munich airport  hour transit time reduced to  minutes  horrible airport experience with no guidance at munich they lost my bag which was did not arrive on  dec in oman day  of lost bag on  jan   i bought the ticket from their website no discount or changes from my end please avoid this airline and muc airport  days and my bag with family gifts for xmas and other essentials is nowhere in site lh tells me to ask the connecting flight operator oman air but my bag is in lh custody which they have not released to oman air lh ground staff at lhr needs more training as well a learning experience for me'
analysis = TextBlob(opinion)
print(analysis.sentiment.polarity)