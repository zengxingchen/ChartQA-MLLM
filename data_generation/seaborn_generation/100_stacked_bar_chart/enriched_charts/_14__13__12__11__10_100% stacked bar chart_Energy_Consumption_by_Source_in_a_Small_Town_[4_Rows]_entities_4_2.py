
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
data = [
    {'Year': 2019, 'Running (%)': 25, 'Cycling (%)': 20, 'Swimming (%)': 30, 'Yoga (%)': 15, 'Weightlifting (%)': 10},
    {'Year': 2020, 'Running (%)': 27, 'Cycling (%)': 18, 'Swimming (%)': 28, 'Yoga (%)': 17, 'Weightlifting (%)': 10},
    {'Year': 2021, 'Running (%)': 30, 'Cycling (%)': 15, 'Swimming (%)': 25, 'Yoga (%)': 20, 'Weightlifting (%)': 10},
    {'Year': 2022, 'Running (%)': 32, 'Cycling (%)': 15, 'Swimming (%)': 22, 'Yoga (%)': 16, 'Weightlifting (%)': 15},
    {'Year': 2023, 'Running (%)': 28, 'Cycling (%)': 18, 'Swimming (%)': 25, 'Yoga (%)': 19, 'Weightlifting (%)': 10}
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
plt.figure(figsize=(12, 8))

# Creating the bar stacks
bottom = None
bar_width = 0.8
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

# Add legend
plt.legend(title="Fitness Activity", bbox_to_anchor=(1.05, 1), loc='upper left')

# Formatting the plot
plt.title('Fitness Activities Distribution Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Activity Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()  # Remove the top and right spines

# Show the plot
plt.show()