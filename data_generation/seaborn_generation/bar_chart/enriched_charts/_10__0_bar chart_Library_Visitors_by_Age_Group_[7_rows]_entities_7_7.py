
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus'],
    'Average Annual Rainfall (mm)': [1200, 380, 990, 1260, 210, 1060, 880, 260, 940, 390, 860, 1350, 940, 1010]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Set the dimensions of the figure
plt.figure(figsize=(12, 10))

# Create the bar chart
bar_plot = sns.barplot(
    x='City',
    y='Average Annual Rainfall (mm)',
    data=df,
    palette=['#4169E1', '#4682B4', '#5F9EA0', '#6495ED', '#00BFFF', '#1E90FF', '#00CED1', '#40E0D0', '#20B2AA', '#87CEFA', '#B0E0E6', '#ADD8E6', '#48D1CC', '#00FFFF'],
    linewidth=0.9,
    edgecolor='black'
)

# Customize the bar widths
for bar in bar_plot.patches:
    bar.set_width(0.6)

# Set the labels and title
plt.xlabel('City')
plt.ylabel('Average Annual Rainfall (mm)')
plt.title('Average Annual Rainfall in Various Cities')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()