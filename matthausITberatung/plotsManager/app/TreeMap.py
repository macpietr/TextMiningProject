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


# Data preparation
labels = []
parents = []
values = []
colors = ['blue', 'green', 'purple']

for airline, clusters in dictOfDictsOfAirlinesClustersCountedWords.items():
    labels.append(airline)
    parents.append('')
    values.append(sum(clusters.values()))

    for cluster, count in clusters.items():
        labels.append(f"{airline} - Cluster_{cluster+1}")
        parents.append(airline)
        values.append(count)

# Create treemap plot
fig = px.treemap(
    names=labels,
    parents=parents,
    values=values,
    title='Treemap of airlines and their clusters',
    branchvalues="total",  # Child wypełnia całą powierzchnię parent
    color_discrete_sequence=colors,  # Kolory dla klastrów
)

# Print plot
fig.update_traces(root_color="lightgrey")
fig.show()