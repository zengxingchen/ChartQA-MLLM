
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Initialize the list of dictionaries with the given data
data = [
    {'Year': 2017, 'Paper': 12000, 'Glass': 8000, 'Metal': 5000, 'Plastic': 4000},
    {'Year': 2018, 'Paper': 13000, 'Glass': 8500, 'Metal': 5500, 'Plastic': 4500},
    {'Year': 2019, 'Paper': 14000, 'Glass': 9000, 'Metal': 6000, 'Plastic': 5000},
    {'Year': 2020, 'Paper': 15000, 'Glass': 9500, 'Metal': 6500, 'Plastic': 6000},
    {'Year': 2021, 'Paper': 16000, 'Glass': 10000, 'Metal': 7000, 'Plastic': 7000}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Set 'Year' as the index
df.set_index('Year', inplace=True)

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))

# Variable to hold cumulative values
cumulative = df.cumsum(axis=1)

# Colors for each category
colors = sns.color_palette("pastel")

# Build the stackplot
ax.stackplot(df.index, [df[col] for col in df.columns], labels=df.columns, colors=colors, alpha=0.8)

# Beautifying the plot
ax.margins(0, 0)
ax.set_title('Recycling Volumes by Material Over Time', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Volume', fontsize=14)

# Adding the legend
ax.legend(loc='upper left')

plt.tight_layout()

# Show the plot
plt.show()