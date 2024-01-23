import pandas as pd
from textblob import TextBlob

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()
pathsManager = PathsManager()

airline = pathsManager.WIZZ_AIR
clusterNumber = 2

df_topic_opinion = objectsManager.getSavedObject('df_topic_opinion_'+airline+'_'+str(clusterNumber))
df_filtered = df_topic_opinion[df_topic_opinion['Opinion'].str.strip() != '']

###Sentiment for each opinion
pd.set_option('display.max_columns', None)
df_filtered['Sentiment'] = df_filtered['Opinion'].apply(lambda opinion: TextBlob(opinion).sentiment.polarity)
df_filtered.columns = ['Proportion' if col == 'Adjustment' else col for col in df_filtered.columns]
print(df_filtered[['TopicId','Proportion','Opinion','Sentiment']])

###Sentiment for each topic using proportion
def weightedPolarity(opinion, proportion):
    analysis = TextBlob(opinion)
    return analysis.sentiment.polarity * proportion

def weightedSubjectivity(opinion, proportion):
    analysis = TextBlob(opinion)
    return analysis.sentiment.subjectivity * proportion

df_filtered['WeightedPolarity'] = df_filtered.apply(lambda row: weightedPolarity(row['Opinion'], row['Proportion']), axis=1)
df_filtered['WeightedSubjectivity'] = df_filtered.apply(lambda row: weightedSubjectivity(row['Opinion'], row['Proportion']), axis=1)
print(df_filtered)

topic_weightedPolarity = df_filtered.groupby('TopicId')['WeightedPolarity'].sum() / df_filtered.groupby('TopicId')['Proportion'].sum()
topic_weightedSubjectivity = df_filtered.groupby('TopicId')['WeightedSubjectivity'].sum() / df_filtered.groupby('TopicId')['Proportion'].sum()

df_polarity_numberOfOpinions = pd.DataFrame({'TopicPolarity' : topic_weightedPolarity,
                                             'TopicSubjectivity': topic_weightedSubjectivity,
                         'NumberOfRelatedTopics' : df_filtered['TopicId'].value_counts()})\
                         .sort_values(by='NumberOfRelatedTopics', ascending=False)

print(df_polarity_numberOfOpinions)

clusterPolarity = df_filtered['WeightedPolarity'].sum() / df_filtered['Proportion'].sum()
clusterSubjectivity = df_filtered['WeightedSubjectivity'].sum() / df_filtered['Proportion'].sum()

print('### cluster polarity ###')
print(clusterPolarity)
print('### cluster subjectivity ###')
print(clusterSubjectivity)
