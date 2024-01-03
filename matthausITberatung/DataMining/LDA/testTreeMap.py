import plotly.express as px
import pandas as pd

# Twoje dane
data = {
    "Lufthansa": {
        "Airports and Operational aspects": {"Topic1": 40, "Topic2": 20, "Topic3": 30},
        "In-Flight Experience": {"Topic4": 50, "Topic5": 10},
        "Booking and Customer Service": {"Topic6": 60, "Topic7": 25}
    },
    "Ryanair": {
        "Booking and Custmer Service": {"Topic1": 35, "Topic2": 45},
        "Flight Operations and Passenger Experience": {"Topic3": 20, "Topic4": 15, "Topic5": 30},
        "Check-in and Airport Services": {"Topic6": 40}
    },
    "Wizz-Air": {
        "Booking and Customer Service": {"Topic1": 20, "Topic2": 30, "Topic3": 50},
        "Flight Experience and Service": {"Topic4": 25, "Topic5": 35},
        "Check-in and Airport Services": {"Topic6": 45, "Topic7": 55}
    }
}

# Przekształcanie danych na format DataFrame
rows = []
for linia, clusters in data.items():
    for cluster, topics in clusters.items():
        suma_opinii_cluster = sum(topics.values())
        for topic, liczba_opinii in topics.items():
            rows.append([linia, cluster, topic, liczba_opinii, suma_opinii_cluster])

df = pd.DataFrame(rows, columns=["Linia", "Cluster", "Topic", "Opinie", "OpinieCluster"])

# Tworzenie wykresu TreeMap przy użyciu Plotly
fig = px.treemap(df, path=['Linia', 'Cluster', 'Topic'], values='Opinie',
                 title="Treemap opinii dla linii lotniczych według clusterów i topiców",
                 custom_data=['Opinie', 'OpinieCluster'])

# Dodanie liczby opinii do etykiet dla topiców i clusterów
fig.update_traces(texttemplate='%{label}<br>%{customdata[0]}',
                  textposition='middle center',
                  textfont_size=16)
fig.update_layout(height=800, width=800)
# Dodanie liczby opinii dla clusterów
fig.data[0].textinfo = 'label+text+value'
fig.show()