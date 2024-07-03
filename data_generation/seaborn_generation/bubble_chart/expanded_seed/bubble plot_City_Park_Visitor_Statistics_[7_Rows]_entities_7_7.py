
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data provided
data = [
    {'Park Name': 'Riverside Green', 'Year': 2020, 'Visitor Count (Thousands)': 150, 'Average Visitor Satisfaction (1-10)': 8.0, 'Acres': 55},
    {'Park Name': 'Maple Shade Park', 'Year': 2020, 'Visitor Count (Thousands)': 95, 'Average Visitor Satisfaction (1-10)': 7.5, 'Acres': 25},
    {'Park Name': 'Lakeview Commons', 'Year': 2020, 'Visitor Count (Thousands)': 120, 'Average Visitor Satisfaction (1-10)': 8.2, 'Acres': 40},
    {'Park Name': 'Old Town Meadow', 'Year': 2020, 'Visitor Count (Thousands)': 80, 'Average Visitor Satisfaction (1-10)': 6.8, 'Acres': 15},
    {'Park Name': 'Eastern Wetlands', 'Year': 2020, 'Visitor Count (Thousands)': 60, 'Average Visitor Satisfaction (1-10)': 7.0, 'Acres': 50},
    {'Park Name': 'Skyline Point', 'Year': 2020, 'Visitor Count (Thousands)': 200, 'Average Visitor Satisfaction (1-10)': 9.0, 'Acres': 70},
    {'Park Name': 'Harbourfront Escape', 'Year': 2020, 'Visitor Count (Thousands)': 180, 'Average Visitor Satisfaction (1-10)': 8.5, 'Acres': 65}
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(10, 6))
bubble_plot = sns.scatterplot(
    data=df,
    x='Acres',
    y='Average Visitor Satisfaction (1-10)',
    size='Visitor Count (Thousands)',
    hue='Park Name',
    sizes=(100, 1000),  # Bubble size range
    alpha=0.7,
    edgecolor='w',
    palette='Dark2'  # Color palette for different parks
)

plt.title('Park Visitor Statistics - 2020')
plt.xlabel('Park Size (Acres)')
plt.ylabel('Average Visitor Satisfaction (1-10)')

# Show the legend separately
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()