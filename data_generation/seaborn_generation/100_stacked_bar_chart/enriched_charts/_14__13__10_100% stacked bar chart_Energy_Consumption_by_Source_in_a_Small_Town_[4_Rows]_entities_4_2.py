
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
data = [
    {'Year': 2019, 'Carbon Emissions (%)': 20, 'Renewable Energy (%)': 30, 'Waste Management (%)': 15, 'Water Usage (%)': 25, 'Air Quality (%)': 10},
    {'Year': 2020, 'Carbon Emissions (%)': 18, 'Renewable Energy (%)': 35, 'Waste Management (%)': 12, 'Water Usage (%)': 25, 'Air Quality (%)': 10},
    {'Year': 2021, 'Carbon Emissions (%)': 22, 'Renewable Energy (%)': 32, 'Waste Management (%)': 18, 'Water Usage (%)': 20, 'Air Quality (%)': 8},
    {'Year': 2022, 'Carbon Emissions (%)': 25, 'Renewable Energy (%)': 30, 'Waste Management (%)': 20, 'Water Usage (%)': 15, 'Air Quality (%)': 10},
    {'Year': 2023, 'Carbon Emissions (%)': 20, 'Renewable Energy (%)': 33, 'Waste Management (%)': 18, 'Water Usage (%)': 22, 'Air Quality (%)': 7}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Normalize data to 100%
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

# Define colors for each stack
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

# Setup seaborn style
sns.set_style('whitegrid')

# Plotting
plt.figure(figsize=(12, 10))

# Creating the bar stacks
bottom = None
bar_width = 0.8
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

# Add legend
plt.legend(title="Environmental Metrics")

# Formatting the plot
plt.title('Environmental Impact Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Impact (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()  # Remove the top and right spines

# Show the plot
plt.show()