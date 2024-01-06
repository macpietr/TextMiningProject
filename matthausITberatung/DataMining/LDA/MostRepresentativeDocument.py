# Group top 5 sentences under each topic
import pandas as pd

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()

pathsManager = PathsManager()

airline = pathsManager.WIZZ_AIR
clusterNumber = 2

df_topic_sents_keywords = objectsManager.getSavedObject('df_topic_opinions_keywords_'+airline+'_'+str(clusterNumber))

sent_topics_sorteddf_mallet = pd.DataFrame()

sent_topics_outdf_grpd = df_topic_sents_keywords.groupby('Dominant_Topic')

for i, grp in sent_topics_outdf_grpd:
    sent_topics_sorteddf_mallet = pd.concat([sent_topics_sorteddf_mallet,
                                             grp.sort_values(['Perc_Contribution'], ascending=[0]).head(1)],
                                            axis=0)

# Reset Index
sent_topics_sorteddf_mallet.reset_index(drop=True, inplace=True)

# Format
sent_topics_sorteddf_mallet.columns = ['Topic_Num', "Topic_Perc_Contrib", "Keywords", "Text"]

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Show
sent_topics_sorteddf_mallet.head()

print(sent_topics_sorteddf_mallet.head(11))