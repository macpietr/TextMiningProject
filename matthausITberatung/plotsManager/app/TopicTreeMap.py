import plotly.express as px
import pandas as pd

data = {
    "Lufthansa": {
        "In-Flight Experience": {"Class Distinction": 287,
                                 "Seating Comfort": 163,
                                 "Onboard Services Provided by the Crew": 137
                                 },
        "Airports and Operational aspects": {"Flight Delays at Frankfurt Airport": 192,
                                             "Flight Management at Munich Airport": 94,
                                             "Boarding Issues": 71,
                                             "Luggage Services and Staff Interaction": 44
                                             },
        "Booking and Customer Service": {"Flight Cancellation Issues": 88,
                                         "Refund Issues": 54,
                                         "Booking and Ticket Management": 45,
                                         "Booking Process Experience": 26
                                         }
    },
    "Ryanair": {
        "Flight Operations and Passenger Experience": {"Booking Process Issues": 164,
                                                       "Additional Costs and Luggage Issues": 145,
                                                       "Booking Management and Cancellation Experiences": 107,
                                                       "Refund Processes and Customer Communication": 46
                                                       },
        "Booking and Customer Service": {"Crew Efficiency at in-Flight Delays": 189,
                                         "Crew Efficiency at Boarding Delays": 160,
                                         "Passenger Experience of Flight Timeliness": 114,
                                         "Seating Comfort on the Board": 37
                                         },
        "Check-in and Airport Services": {"Check-in Procedures and Fees": 170,
                                          "Flight Timing Information and Online Services": 57,
                                          "Check-in Challenges and Documentation Requirements": 12
                                          }
    },
    "Wizz-Air": {
        "Flight Experience and Timeliness": {"Flight Timeliness": 219,
                                             "Comfort and Quality of Seating": 212,
                                             "Crew Efficiency on Flight Delays": 93,
                                             "Crew Interaction and Passenger Experience": 19
                                             },
        "Check-in and Airport Services": {"Online Check-in and Luggage Handling": 196,
                                          "Extra Charges and Airline Policies": 177,
                                          "Luggage Size Regulations and Customer Support": 50
                                          },
        "Booking and Customer Service": {"Flight Cancellations": 125,
                                         "Booking Process and Customer Support": 61,
                                         "Refunds and Financial Operations": 35,
                                         "Customer Communication and Seats Reservation": 14
                                         }
    }
}


# Convert to DF
rows = []
for linia, clusters in data.items():
    for cluster, topics in clusters.items():
        suma_opinii_cluster = sum(topics.values())
        for topic, liczba_opinii in topics.items():
            rows.append([linia, cluster, topic, liczba_opinii, suma_opinii_cluster])

df = pd.DataFrame(rows, columns=["Airline", "Cluster", "Topic", "OpinionCount", "Opinion-Cluster"])

df['Topic'] = df['Topic'].apply(lambda x: x.replace(' ', '\n'))

# Ploty treemap creation
fig = px.treemap(df, path=['Airline', 'Cluster', 'Topic'], values='OpinionCount',
                 title="Treemap of clusters and their topic proportion",
                 custom_data=['OpinionCount', 'Opinion-Cluster'])

# Add opinion counts to lables
fig.update_traces(texttemplate='%{label}<br>%{customdata[0]}',
                  textposition='middle center',
                  textfont_size=16)
fig.update_layout(height=800, width=800)
fig.show()