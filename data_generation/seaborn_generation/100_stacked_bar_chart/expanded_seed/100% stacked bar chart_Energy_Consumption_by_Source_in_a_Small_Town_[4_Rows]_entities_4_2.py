
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
data = [
    {'Year': 2019, 'Solar (%)': 5, 'Wind (%)': 15, 'Hydro (%)': 10, 'Fossil Fuels (%)': 65, 'Nuclear (%)': 5},
    {'Year': 2020, 'Solar (%)': 7, 'Wind (%)': 18, 'Hydro (%)': 10, 'Fossil Fuels (%)': 60, 'Nuclear (%)': 5},
    {'Year': 2021, 'Solar (%)': 10, 'Wind (%)': 20, 'Hydro (%)': 15, 'Fossil Fuels (%)': 50, 'Nuclear (%)': 5},
    {'Year': 2022, 'Solar (%)': 12, 'Wind (%)': 25, 'Hydro (%)': 15, 'Fossil Fuels (%)': 43, 'Nuclear (%)': 5}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Normalize data to 100%
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

# Define colors for each stack
colors = sns.color_palette('pastel', len(df_normalized.columns))

# Setup seaborn style
sns.set_style('whitegrid')

# Plotting
plt.figure(figsize=(10, 6))

# Creating the bar stacks
bottom = None
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white')
    bottom = columnData if bottom is None else bottom + columnData

# Add legend
plt.legend(title="Energy Source")

# Formatting the plot
plt.title('Energy Composition over Years')
plt.xlabel('Year')
plt.ylabel('Energy Source Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()  # Remove the top and right spines

# Show the plot
plt.show()