import pandas as pd
import plotly.express as px

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()
pathsManager = PathsManager()

dictOfDictsOfAirlinesClustersOpinions = objectsManager.getSavedObject('dictOfDictsOfAirlinesClustersOpinions')

word_count_structure = {}

dictOfDictsOfAirlinesClustersCountedWords = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dictOfClustersCountedWords = {}
    for cluster in dictOfDictsOfAirlinesClustersOpinions[airline]:
        total_word_count = 0
        for opinion in dictOfDictsOfAirlinesClustersOpinions[airline][cluster]:
            total_word_count += len(opinion.split())
        dictOfClustersCountedWords[cluster] = total_word_count
    dictOfDictsOfAirlinesClustersCountedWords[airline] = dictOfClustersCountedWords

print(dictOfDictsOfAirlinesClustersCountedWords)

dictOfDictsOfAirlinesClustersCountedDocs = {}
for airline in pathsManager.LIST_OF_AIRLINES:
    dictOfClustersCountedDocs = {}
    for cluster in dictOfDictsOfAirlinesClustersOpinions[airline]:
        dictOfClustersCountedDocs[cluster] = len(dictOfDictsOfAirlinesClustersOpinions[airline][cluster])
    dictOfDictsOfAirlinesClustersCountedDocs[airline] = dictOfClustersCountedDocs

print(dictOfDictsOfAirlinesClustersCountedDocs)

clusterLabels = ['Airports and Operational Aspects',
                 'In-Flight Experience',
                 'Booking and Customer Service',
                 'Booking and Customer Service',
                 'Flight Operations and Passenger Experience',
                 'Check-in and Airport Services',
                 'Booking and Customer Service',
                 'Flight Experience and Service',
                 'Check-in and Airport Services']

colors = ['blue', 'green', 'purple']

rows = []
for airline, clusters in dictOfDictsOfAirlinesClustersCountedDocs.items():
    for cluster, count in clusters.items():
        rows.append([airline, cluster, count])

df = pd.DataFrame(rows, columns=["Airline", "Cluster", "Count"])

df['Cluster'] = clusterLabels

fig = px.treemap(df, path=["Airline", "Cluster"],
                 values="Count",
                 title="Amonts of documets per cluster",
                 color_discrete_sequence=colors,
                 custom_data=["Count"])

fig.update_traces(texttemplate='%{label}<br>%{customdata[0]}',
                  textposition='middle center',
                  textfont_size=16)
fig.update_layout(height=800, width=800)

# Print plot
fig.update_traces(root_color="lightgrey")
fig.data[0].textinfo = 'label+text+value'
fig.show()