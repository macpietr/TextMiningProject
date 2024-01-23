import pandas as pd
import plotly.express as px

topicData = {
    "Airline": ["Lufthansa", "Lufthansa", "Lufthansa", "Lufthansa", "Lufthansa",
                "Ryanair", "Ryanair", "Ryanair", "Ryanair", "Ryanair",
                "Wizz-Air", "Wizz-Air", "Wizz-Air", "Wizz-Air", "Wizz-Air"],
    "Dimension": ["Tangibles", "Reliability", "Responsiveness", "Assurance", "Empathy",
                  "Tangibles", "Reliability", "Responsiveness", "Assurance", "Empathy",
                  "Tangibles", "Reliability", "Responsiveness", "Assurance", "Empathy"],
    "Dimension Score": [3.55, 2.90, 2.98, 3.05, 3.30,
                 3.73, 3.22, 3.12, 2.90, 3.09,
                 3.30, 3.09, 2.88, 3.15, 2.87],
    "Dimension Proportion(%)": [7.97+5.52, 1.97+2.44, 5.33+1.50+1.25, 1.22+0.72, 2.61+3.80,
                       1.03, 2.97+3.16+0.33, 1.28+5.25, 4.55+1.58, 4.02+4.44+4.72,
                       5.88, 3.47+6.08+5.44, 0.97+0.39+4.91, 2.58+0.53, 1.69+1.39]
}

df = pd.DataFrame(topicData)

fig = px.scatter(df, x="Dimension Proportion(%)", y="Dimension Score", color="Airline", symbol="Dimension",
                 title="SERVQUAL Score and Proportion",
                 size_max=50)  # Increase marker size

# Update layout for larger font
fig.update_layout(
    title_font_size=10,
    font_size=10,
    legend_title_font_size=10
)

# Displaying the updated figure
fig.show()