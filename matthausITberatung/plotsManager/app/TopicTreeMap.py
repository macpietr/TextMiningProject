import plotly.express as px
import pandas as pd
from _plotly_utils.colors.qualitative import Plotly

data = {
    "Lufthansa": {
        "In-Flight Experience": {"Class Distinction": 287,
                                 "Seating Comfort": 163,
                                 "Onboard Services<br>Provided by the Crew": 137
                                 },
        "Airports and Operational aspects": {"Flight Delays at<br>Frankfurt Airport": 192,
                                             "Flight Management at<br>Munich Airport": 94,
                                             "Boarding Issues": 71,
                                             "Luggage Services and<br>Staff Interaction": 44
                                             },
        "Booking and Customer Service": {"Flight Cancellation<br>Issues": 88,
                                         "Refund Issues": 54,
                                         "Booking and Ticket<br>Management": 45,
                                         "Booking Process<br>Experience": 26
                                         }
    },
    "Ryanair": {
        "Flight Operations and Passenger Experience": {"Booking Process Issues": 164,
                                                       "Additional Costs and<br>uggage Issues": 145,
                                                       "Booking Management and<br>Cancellation Experiences": 107,
                                                       "Refund<br>Processes and<br>Customer Communication": 46
                                                       },
        "Booking and Customer Service": {"Crew Efficiency at<br>in-Flight Delays": 189,
                                         "Crew Efficiency at<br>Boarding Delays": 160,
                                         "Passenger Experience of<br>Flight Timeliness": 114,
                                         "Seating<br>on the Board": 37
                                         },
        "Check-in and Airport Services": {"Check-in Procedures<br>and Fees": 170,
                                          "Flight Timing Information<br>and Online Services": 57,
                                          "Check-in Challenges and<br>Documentation Requirements": 12
                                          }
    },
    "Wizz-Air": {
        "Flight Experience and Timeliness": {"Flight Timeliness": 219,
                                             "Comfort and Quality<br>of Seating": 212,
                                             "Crew Efficiency on<br>Flight Delays": 93,
                                             "Crew Interaction and<br>Passenger Experience": 19
                                             },
        "Check-in and Airport Services": {"Online Check-in and<br>Luggage Handling": 196,
                                          "Extra Charges and<br>Airline Policies": 177,
                                          "Luggage Size<br>Regulations and<br>Customer Support": 50
                                          },
        "Booking and Customer Service": {"Flight<br>Cancellations": 125,
                                         "Booking<br>Process and<br>Customer Support": 61,
                                         "Refunds and Financial<br>Operations": 35,
                                         "Customer Communication<br>and Seats Reservation": 14
                                         }
    }
}
colors = [Plotly[4], Plotly[5], Plotly[3]]

# colors = ['blue', 'green', 'purple']

# Convert to DF
rows = []
for airline, clusters in data.items():
    for cluster, topics in clusters.items():
        cluster_opinions_sum = sum(topics.values())
        for topic, number_of_opinions in topics.items():
            rows.append([airline, cluster, topic, number_of_opinions, cluster_opinions_sum])

df = pd.DataFrame(rows, columns=["Airline", "Cluster", "Topic", "OpinionCount", "Opinion-Cluster"])

df['Topic'] = df['Topic'].apply(lambda x: x.replace(' ', '\n'))
df['OpinionCount'] = df['OpinionCount'].apply(lambda x: round(x/36.03,2))

# Ploty treemap creation
fig = px.treemap(df, path=['Airline', 'Cluster', 'Topic'], values='OpinionCount',
                 title="Treemap of clusters and their topic proportion",
                 custom_data=['OpinionCount', 'Opinion-Cluster'],
                 color_discrete_sequence=colors)

# Add opinion counts to lables
fig.update_traces(texttemplate='%{label}<br>%{customdata[0]}',
                  textposition='middle center',
                  textfont_size=16)
fig.update_layout(uniformtext=dict(minsize=16, mode='show'))
fig.update_layout(height=2000, width=1300)
fig.show()