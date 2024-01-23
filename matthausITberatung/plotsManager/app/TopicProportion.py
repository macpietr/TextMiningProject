import pandas as pd
import matplotlib.pyplot as plt
from _plotly_utils.colors.qualitative import Dark24

# Create dataframe from the given data
data = {
    'Cluster': [
        'In-Flight Experience', 'In-Flight Experience', 'In-Flight Experience',
        'Airports and Operational aspects', 'Airports and Operational aspects',
        'Airports and Operational aspects', 'Airports and Operational aspects',
        'Booking and Customer Service_Lufthansa', 'Booking and Customer Service_Lufthansa',
        'Booking and Customer Service_Lufthansa', 'Booking and Customer Service_Lufthansa',
        'Flight Operations and Passenger Experience', 'Flight Operations and Passenger Experience',
        'Flight Operations and Passenger Experience', 'Flight Operations and Passenger Experience',
        'Booking and Customer Service_Ryanair', 'Booking and Customer Service_Ryanair',
        'Booking and Customer Service_Ryanair', 'Booking and Customer Service_Ryanair',
        'Check-in and Airport Services_Ryanair', 'Check-in and Airport Services_Ryanair',
        'Check-in and Airport Services_Ryanair', 'Flight Experience and Timeliness',
        'Flight Experience and Timeliness', 'Flight Experience and Timeliness',
        'Flight Experience and Timeliness', 'Check-in and Airport Services_WizzAir',
        'Check-in and Airport Services_WizzAir', 'Check-in and Airport Services_WizzAir',
        'Booking and Customer Service_WizzAir', 'Booking and Customer Service_WizzAir',
        'Booking and Customer Service_WizzAir', 'Booking and Customer Service_WizzAir'
    ],
    'Cluster Polarity': [
        0.180984, 0.180984, 0.180984,
        -0.010215, -0.010215, -0.010215, -0.010215,
        -0.003495, -0.003495, -0.003495, -0.003495,
        -0.012348, -0.012348, -0.012348, -0.012348,
        0.126398, 0.126398, 0.126398, 0.126398,
        -0.012725, -0.012725, -0.012725,
        0.117463, 0.117463, 0.117463, 0.117463,
        -0.046799, -0.046799, -0.046799,
        -0.061164, -0.061164, -0.061164, -0.061164
    ],
    'Topic': [
        'Class Distinction', 'Seating Comfort', 'Onboard Services Provided by the Crew',
        'Flight Delays at Frankfurt Airport', 'Flight Management at Munich Airport',
        'Boarding Issues', 'Luggage Services and Staff Interaction',
        'Flight Cancellation Issues', 'Refund Issues',
        'Booking and Ticket Management', 'Booking Process Experience',
        'Booking Process Issues', 'Additional Costs and Luggage Issues',
        'Booking Management and Cancellation Experiences', 'Refund Processes and Customer Communication',
        'Crew Efficiency at in-Flight Delays', 'Crew Efficiency at Boarding Delays',
        'Passenger Experience of Flight Timeliness', 'Seating on the Board',
        'Check-in Procedures and Fees', 'Flight Timing Information and Online Services',
        'Check-in Challenges and Documentation Requirements', 'Flight Timeliness',
        'Comfort and Quality of Seating', 'Crew Efficiency on Flight Delays',
        'Crew Interaction and Passenger Experience', 'Online Check-in and Luggage Handling',
        'Extra Charges and Airline Policies', 'Luggage Size Regulations and Customer Support',
        'Flight Cancellations', 'Booking Process and Customer Support',
        'Refunds and Financial Operations', 'Customer Communication and Seats Reservation'
    ],
    'Topic Polarity': [0.192953,0.169584,0.170075,-0.009606,
        -0.003613,-0.043891,0.026173,-0.026744,-0.006746,0.045257,0.002373,-0.032566,-0.017357,0.021089,-0.003367,
        0.106398,0.113797,0.134138,0.243663,-0.006932,-0.035389,
        0.008272,0.170514,0.098438,0.034052,0.129331,-0.060046,-0.046610,-0.004279,-0.074483,-0.072270,-0.028430,0.019613
    ]
}

df = pd.DataFrame(data)

colors = {'In-Flight Experience' : Dark24[0],
'Airports and Operational aspects' : Dark24[4],
'Booking and Customer Service_Lufthansa' : Dark24[8],
'Flight Operations and Passenger Experience' : Dark24[10],
'Booking and Customer Service_Ryanair' : Dark24[13],
'Check-in and Airport Services_Ryanair' : Dark24[16],
'Flight Experience and Timeliness' : Dark24[19],
'Check-in and Airport Services_WizzAir' : Dark24[23],
'Booking and Customer Service_WizzAir' : Dark24[18]
}

sorted_df = df.sort_index(ascending=False)
fig, ax = plt.subplots(figsize=(14, 10))

# Add bars for topics and collect the y positions for cluster names/polarities
cluster_y_positions = {}
for i, row in sorted_df.iterrows():
    bar = ax.barh(row['Topic'], row['Topic Polarity'], color=colors[row['Cluster']], edgecolor='black')
    # Record the position for the cluster name and polarity
    if row['Cluster'] not in cluster_y_positions:
        cluster_y_positions[row['Cluster']] = (bar[0].get_y() + bar[0].get_height() / 2)

# Add cluster names and polarities in the plot
for cluster, y_pos in cluster_y_positions.items():
    cluster_polarity = sorted_df[sorted_df['Cluster'] == cluster]['Cluster Polarity'].iloc[0]
    # Position the cluster name and polarity on the right empty space of the plot
    ax.text(max(sorted_df['Topic Polarity']) + 0.02, y_pos,
            f"{cluster}\n{cluster_polarity:.2f}", fontsize=12, weight='bold',
            color=colors[cluster], ha='left', va='center')

# Set labels and title
ax.set_xlabel('Polarity', fontsize=14)
ax.set_title('Topic Polarity Grouped by Clusters', fontsize=16)
ax.set_yticks(range(len(sorted_df['Topic'])))
ax.set_yticklabels(sorted_df['Topic'], fontsize=12)

# Save the plot to a file
plt.tight_layout()
plt.show()