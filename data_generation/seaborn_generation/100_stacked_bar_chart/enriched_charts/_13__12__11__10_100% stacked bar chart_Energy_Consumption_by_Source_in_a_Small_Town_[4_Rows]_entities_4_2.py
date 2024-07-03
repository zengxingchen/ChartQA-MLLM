
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
data = [
    {'Year': 2019, 'Reading (%)': 20, 'Writing (%)': 25, 'Research (%)': 30, 'Discussion (%)': 15, 'Presentation (%)': 10},
    {'Year': 2020, 'Reading (%)': 22, 'Writing (%)': 27, 'Research (%)': 28, 'Discussion (%)': 13, 'Presentation (%)': 10},
    {'Year': 2021, 'Reading (%)': 25, 'Writing (%)': 20, 'Research (%)': 25, 'Discussion (%)': 20, 'Presentation (%)': 10},
    {'Year': 2022, 'Reading (%)': 30, 'Writing (%)': 15, 'Research (%)': 20, 'Discussion (%)': 20, 'Presentation (%)': 15},
    {'Year': 2023, 'Reading (%)': 28, 'Writing (%)': 20, 'Research (%)': 22, 'Discussion (%)': 20, 'Presentation (%)': 10}
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
plt.figure(figsize=(10, 6))

# Creating the bar stacks
bottom = None
bar_width = 0.6
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

# Add legend
plt.legend(title="Academic Activity", bbox_to_anchor=(1.05, 1), loc='upper left')

# Formatting the plot
plt.title('Academic Activities Distribution Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Activity Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()  # Remove the top and right spines

# Show the plot
plt.show()