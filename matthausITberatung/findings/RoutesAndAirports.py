import pandas as pd

airlines_data = {
    'Airlines': ['Lufthansa', 'Ryanair', 'Wizz-Air'],
    'Number of distinct routes': [649, 927, 642],
    'Number of distinct airports': [333, 382, 296]
}

# Convert to a DataFrame
df_airlines = pd.DataFrame(airlines_data)

# Calculate the maximum and minimum values for scaling
max_routes = df_airlines['Number of distinct routes'].max()
min_routes = df_airlines['Number of distinct routes'].min()
max_airports = df_airlines['Number of distinct airports'].max()
min_airports = df_airlines['Number of distinct airports'].min()

# Define new scale min and max
new_scale_min = 2
new_scale_max = 4

# Function to scale the values from 2 to 4
def scale_value(value, min_value, max_value, new_min, new_max):
    return ((value - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min

# Scale the values from 2 to 4
df_airlines['Routes'] = df_airlines['Number of distinct routes'].apply(
    lambda x: scale_value(x, min_routes, max_routes, new_scale_min, new_scale_max))
df_airlines['Airports'] = df_airlines['Number of distinct airports'].apply(
    lambda x: scale_value(x, min_airports, max_airports, new_scale_min, new_scale_max))

print(df_airlines)