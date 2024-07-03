
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
data = [
    {'Year': 2019, 'Work (%)': 30, 'Exercise (%)': 15, 'Sleep (%)': 35, 'Leisure (%)': 10, 'Meditation (%)': 10},
    {'Year': 2020, 'Work (%)': 32, 'Exercise (%)': 18, 'Sleep (%)': 30, 'Leisure (%)': 10, 'Meditation (%)': 10},
    {'Year': 2021, 'Work (%)': 35, 'Exercise (%)': 20, 'Sleep (%)': 25, 'Leisure (%)': 12, 'Meditation (%)': 8},
    {'Year': 2022, 'Work (%)': 33, 'Exercise (%)': 22, 'Sleep (%)': 28, 'Leisure (%)': 10, 'Meditation (%)': 7},
    {'Year': 2023, 'Work (%)': 31, 'Exercise (%)': 25, 'Sleep (%)': 24, 'Leisure (%)': 15, 'Meditation (%)': 5}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Normalize data to 100%
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

# Define colors for each stack
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f']

# Setup seaborn style
sns.set_style('whitegrid')

# Plotting
plt.figure(figsize=(12, 8))

# Creating the bar stacks
bottom = None
bar_width = 0.7
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

# Add legend
plt.legend(title="Health Activity", bbox_to_anchor=(1.05, 1), loc='upper left')

# Formatting the plot
plt.title('Health Routine Distribution Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Activity Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()  # Remove the top and right spines

# Show the plot
plt.show()