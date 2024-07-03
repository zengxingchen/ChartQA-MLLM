
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    {'Day': 'Monday', 'Renewable Energy': 0.20, 'Conservation': 0.15, 'Climate Change': 0.18, 'Pollution Control': 0.22, 'Wildlife Protection': 0.15, 'Environmental Education': 0.10},
    {'Day': 'Tuesday', 'Renewable Energy': 0.22, 'Conservation': 0.18, 'Climate Change': 0.15, 'Pollution Control': 0.20, 'Wildlife Protection': 0.15, 'Environmental Education': 0.10},
    {'Day': 'Wednesday', 'Renewable Energy': 0.18, 'Conservation': 0.20, 'Climate Change': 0.17, 'Pollution Control': 0.15, 'Wildlife Protection': 0.20, 'Environmental Education': 0.10},
    {'Day': 'Thursday', 'Renewable Energy': 0.15, 'Conservation': 0.18, 'Climate Change': 0.20, 'Pollution Control': 0.15, 'Wildlife Protection': 0.20, 'Environmental Education': 0.12},
    {'Day': 'Friday', 'Renewable Energy': 0.25, 'Conservation': 0.20, 'Climate Change': 0.15, 'Pollution Control': 0.15, 'Wildlife Protection': 0.12, 'Environmental Education': 0.13},
    {'Day': 'Saturday', 'Renewable Energy': 0.22, 'Conservation': 0.15, 'Climate Change': 0.18, 'Pollution Control': 0.20, 'Wildlife Protection': 0.10, 'Environmental Education': 0.15},
    {'Day': 'Sunday', 'Renewable Energy': 0.20, 'Conservation': 0.17, 'Climate Change': 0.18, 'Pollution Control': 0.15, 'Wildlife Protection': 0.15, 'Environmental Education': 0.15}
]

# Transform data into a pandas DataFrame
df = pd.DataFrame(data)

# Prepare data for 100% stacked bar chart
df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

# Calculate cumulative sum for stacking
cumsum_df = df.cumsum(axis=1)

# Start plotting
fig, ax = plt.subplots(figsize=(8, 12))

# Plotting each layer of the stacked bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF6', '#FF8C33']
width = 0.8  # Change the width of the bars
for i, col in enumerate(df.columns):
    ax.barh(df.index, df[col], left=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', height=width)

# Customizing the plot
plt.xticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Percentage')
plt.ylabel('Day of the Week')
plt.title('Environmental Activities by Day', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()