# Number of Documents for Each Topic
import pandas as pd

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

pathsManager = PathsManager()
objectsManager = ObjectsManager()

airline = pathsManager.LUFTHANSA
clusterNumber = 0
numberOfTopics = 4

df_topic_sents_keywords = objectsManager.getSavedObject('df_topic_opinions_keywords_'+airline+'_'+str(clusterNumber))

topic_counts = df_topic_sents_keywords['Dominant_Topic'].value_counts()

# Percentage of Documents for Each Topic
topic_contribution = round(topic_counts/topic_counts.sum(), numberOfTopics)

# Topic Number and Keywords
topic_num_keywords = df_topic_sents_keywords[['Dominant_Topic', 'Topic_Keywords']]

# Concatenate Column wise
df_dominant_topics = pd.concat([topic_num_keywords, topic_counts, topic_contribution], axis=1)

# Change Column names
df_dominant_topics.columns = ['Dominant_Topic', 'Topic_Keywords', 'Num_Documents', 'Perc_Documents']

pd.set_option('display.max_rows', 8)
pd.set_option('display.max_columns', None)

# Show
print(df_dominant_topics)