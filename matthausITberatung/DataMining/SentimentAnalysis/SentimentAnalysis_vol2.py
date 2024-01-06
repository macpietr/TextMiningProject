import pandas as pd
from textblob import TextBlob

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

objectsManager = ObjectsManager()
topicModelling = objectsManager.getSavedObject('topicModelling_lufthansa_0')
df_topic_opinion = objectsManager.getSavedObject('df_topic_opinion_lufthansa_0')
df_filtered = df_topic_opinion[df_topic_opinion['Opinion'].str.strip() != '']

###Sentiment for each opinion
pd.set_option('display.max_columns', None)
df_filtered['Sentiment'] = df_filtered['Opinion'].apply(lambda opinion: TextBlob(opinion).sentiment.polarity)
df_filtered.columns = ['Proportion' if col == 'Adjustment' else col for col in df_filtered.columns]
print(df_filtered[['TopicId','Proportion','Opinion','Sentiment']])

##TODO: I have used the average with proportion included approach
###Sentiment for each topic using proportion
def weightedPolarity(opinion, proportion):
    analysis = TextBlob(opinion)
    return analysis.sentiment.polarity * proportion

df_filtered['WeightedPolarity'] = df_filtered.apply(lambda row: weightedPolarity(row['Opinion'], row['Proportion']), axis=1)
print(df_filtered)

topic_weightedPolaity = df_filtered.groupby('TopicId')['WeightedPolarity'].sum() / df_filtered.groupby('TopicId')['Proportion'].sum()
df_topic_weightedPolaity = pd.DataFrame({'TopicId': topic_weightedPolaity.index, 'WeightedPolarity': topic_weightedPolaity.values})
print(df_topic_weightedPolaity)


####Sentiment for cluster - a co z topic proportion?
cluster_polarity = df_topic_weightedPolaity['WeightedPolarity'].mean()
print(cluster_polarity)
