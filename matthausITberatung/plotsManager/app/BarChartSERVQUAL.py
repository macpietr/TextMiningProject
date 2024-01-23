import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the provided data
from _plotly_utils.colors.qualitative import Plotly

topicData = {
    "Airline": ["Lufthansa", "Lufthansa", "Lufthansa", "Lufthansa", "Lufthansa",
                "Ryanair", "Ryanair", "Ryanair", "Ryanair", "Ryanair",
                "Wizz-Air", "Wizz-Air", "Wizz-Air", "Wizz-Air", "Wizz-Air"],
    "Dimension": ["Tangibles", "Reliability", "Responsiveness", "Assurance", "Empathy",
                  "Tangibles", "Reliability", "Responsiveness", "Assurance", "Empathy",
                  "Tangibles", "Reliability", "Responsiveness", "Assurance", "Empathy"],
    "Dim Mark": [3.55, 2.90, 2.98, 3.05, 3.30,
                 3.73, 3.22, 3.12, 2.90, 3.09,
                 3.30, 3.09, 2.88, 3.15, 2.87]
}

# title = 'SERVQUAL for Topics'

preDefCatData = {
    "Airline": ["Lufthansa", "Lufthansa", "Lufthansa", "Lufthansa", "Lufthansa",
                "Ryanair", "Ryanair", "Ryanair", "Ryanair", "Ryanair",
                "Wizz-Air", "Wizz-Air", "Wizz-Air", "Wizz-Air", "Wizz-Air"],
    "Dimension": ["Tangibles", "Reliability", "Responsiveness", "Assurance", "Empathy",
                  "Tangibles", "Reliability", "Responsiveness", "Assurance", "Empathy",
                  "Tangibles", "Reliability", "Responsiveness", "Assurance", "Empathy"],
    "Dim Mark": [3.02,2.75,2.92,2.55,2.5,
                 1.72,3.50,2.26,2.33,2,
                 1.72,2.57,2.06,2.18,2]
}

title = 'SERVQUAL for Predefined Categories'

colors = {'Lufthansa': Plotly[4], 'Ryanair': Plotly[5], 'Wizz-Air': Plotly[3]}

df = pd.DataFrame(preDefCatData)



# Set the positions and width for the bars
positions = range(len(df['Dimension'].unique()))
width = 0.25  # the width of the bars

# Plotting the bars next to each other for each group
fig, ax = plt.subplots(figsize=(12, 7))

# Create bars for each airline in each dimension
for i, dimension in enumerate(df['Dimension'].unique()):
    # Filter the data for each dimension
    dimension_data = df[df['Dimension'] == dimension]
    # Create bars for each airline
    for j, airline in enumerate(dimension_data['Airline'].unique()):
        # Calculate the position for each airline's bar
        position = [p + (j - 1) * width for p in positions if df['Dimension'].unique()[p] == dimension]
        # Extract the data for the current airline and dimension
        airline_data = dimension_data[dimension_data['Airline'] == airline]
        # Plot the bar for the airline
        ax.bar(position, airline_data['Dim Mark'], width, label=airline if i == 0 else "", color=colors[airline])

# Set the position and labels for the x-axis
ax.set_xticks([p + width for p in positions])
ax.set_xticklabels(df['Dimension'].unique())

# Place the legend
ax.legend(fontsize=12)


# Adding labels and title
ax.set_xticklabels(df['Dimension'].unique(), fontsize=14)
ax.set_xlabel('Service Dimension', fontsize=16)
ax.set_ylabel('Dimension Mark', fontsize=16)
ax.set_title(title, fontsize=18)
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels

# Show the plot
plt.show()