
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = [
    {'Week': 'Week 1', ' Price (USD)': 3.49}, 
    {'Week': 'Week 2', ' Price (USD)': 3.55},
    {'Week': 'Week 3', ' Price (USD)': 3.6}, 
    {'Week': 'Week 4', ' Price (USD)': 3.58},
    {'Week': 'Week 5', ' Price (USD)': 3.62}, 
    {'Week': 'Week 6', ' Price (USD)': 3.67},
    {'Week': 'Week 7', ' Price (USD)': 3.65}, 
    {'Week': 'Week 8', ' Price (USD)': 3.7},
    {'Week': 'Week 9', ' Price (USD)': 3.75}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Rename the ' Price (USD)' column to remove leading space
df.rename(columns={' Price (USD)': 'Price (USD)'}, inplace=True)

# Set the styling using Seaborn
sns.set(style="whitegrid")

# Plot the area chart using plt.fill_between() on the matplotlib axis
fig, ax = plt.subplots(figsize=(10, 6))

# Line plot for the border of the area chart
sns.lineplot(ax=ax, x='Week', y='Price (USD)', data=df, color="darkblue", lw=2)

# Use fill_between to create the filled area effect
ax.fill_between(df['Week'], df['Price (USD)'], color="skyblue", alpha=0.4)

# Additional customizations
ax.set_title('Weekly Price (USD)', fontsize=16)
ax.set_xlabel('Week', fontsize=12)
ax.set_ylabel('Price (USD)', fontsize=12)

# Tight layout for better spacing
plt.tight_layout()

# Show plot
plt.show()