
import pandas as pd
import matplotlib.pyplot as plt

# Given dataset
data = [
    {'Week': 'Jan 1-7', ' Coffee': 2300, ' Pastries': 1200, ' Sandwiches': 800, ' Salads': 600},
    {'Week': 'Jan 8-14', ' Coffee': 2100, ' Pastries': 1300, ' Sandwiches': 850, ' Salads': 450},
    {'Week': 'Jan 15-21', ' Coffee': 2200, ' Pastries': 1400, ' Sandwiches': 900, ' Salads': 500},
    {'Week': 'Jan 22-28', ' Coffee': 2400, ' Pastries': 1500, ' Sandwiches': 950, ' Salads': 700},
    {'Week': 'Feb 1-7', ' Coffee': 2500, ' Pastries': 1600, ' Sandwiches': 1000, ' Salads': 750},
    {'Week': 'Feb 8-14', ' Coffee': 2600, ' Pastries': 1700, ' Sandwiches': 1100, ' Salads': 800},
    {'Week': 'Feb 15-21', ' Coffee': 2300, ' Pastries': 1300, ' Sandwiches': 900, ' Salads': 650},
    {'Week': 'Feb 22-28', ' Coffee': 2200, ' Pastries': 1250, ' Sandwiches': 950, ' Salads': 600},
    {'Week': 'Mar 1-7', ' Coffee': 2100, ' Pastries': 1350, ' Sandwiches': 1000, ' Salads': 550},
    {'Week': 'Mar 8-14', ' Coffee': 2400, ' Pastries': 1450, ' Sandwiches': 1050, ' Salads': 750},
    {'Week': 'Mar 15-21', ' Coffee': 2300, ' Pastries': 1500, ' Sandwiches': 1100, ' Salads': 800},
    {'Week': 'Mar 22-28', ' Coffee': 2200, ' Pastries': 1550, ' Sandwiches': 1150, ' Salads': 850}
]

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Set the 'Week' column as index
df.set_index('Week', inplace=True)

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 6))
columns = df.columns
# Starting from the bottom, cumulatively add the heights of the bars
for i, column in enumerate(columns[::-1]):
    ax.fill_between(df.index, df[columns[:len(columns)-i]].sum(axis=1), label=column)

# Formatting the plot
ax.set_title('Sales Data by Product and Week')
ax.set_xlabel('Week')
ax.set_ylabel('Units Sold')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()