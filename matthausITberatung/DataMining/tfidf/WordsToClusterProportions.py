from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

dictonary = ObjectsManager().getSavedObject('dictOfDictsOfAirlinesClustersOpinions')

# Opinions of cluster
cluster_opinions = dictonary['lufthansa'][0]

# cluster corpus
cluster_corpus = ' '.join(cluster_opinions)

# Create CountVectorizer
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform([cluster_corpus])

# get dictionary word-index
index_to_word = {i: word for word, i in vectorizer.vocabulary_.items()}

# get amount of every single word
word_counter = Counter(cluster_corpus.split())

# 30 most common words and their proportion
for word, amount in word_counter.most_common(30):
    proportion = amount / len(cluster_corpus.split())
    print(f'{word}: {proportion:.4f}')