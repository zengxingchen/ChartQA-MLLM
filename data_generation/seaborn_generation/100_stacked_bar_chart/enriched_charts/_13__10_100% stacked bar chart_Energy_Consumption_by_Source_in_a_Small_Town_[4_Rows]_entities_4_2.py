
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
data = [
    {'Year': 2019, 'Fruits (%)': 25, 'Vegetables (%)': 30, 'Grains (%)': 20, 'Proteins (%)': 15, 'Dairy (%)': 10},
    {'Year': 2020, 'Fruits (%)': 28, 'Vegetables (%)': 25, 'Grains (%)': 22, 'Proteins (%)': 15, 'Dairy (%)': 10},
    {'Year': 2021, 'Fruits (%)': 27, 'Vegetables (%)': 30, 'Grains (%)': 18, 'Proteins (%)': 15, 'Dairy (%)': 10},
    {'Year': 2022, 'Fruits (%)': 30, 'Vegetables (%)': 28, 'Grains (%)': 20, 'Proteins (%)': 12, 'Dairy (%)': 10},
    {'Year': 2023, 'Fruits (%)': 26, 'Vegetables (%)': 32, 'Grains (%)': 22, 'Proteins (%)': 12, 'Dairy (%)': 8}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Normalize data to 100%
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

# Define colors for each stack
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Setup seaborn style
sns.set_style('whitegrid')

# Plotting
plt.figure(figsize=(10, 8))

# Creating the bar stacks
bottom = None
bar_width = 0.7
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

# Add legend
plt.legend(title="Diet Composition")

# Formatting the plot
plt.title('Distribution of Food Categories in Diet Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Composition (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()  # Remove the top and right spines

# Show the plot
plt.show()