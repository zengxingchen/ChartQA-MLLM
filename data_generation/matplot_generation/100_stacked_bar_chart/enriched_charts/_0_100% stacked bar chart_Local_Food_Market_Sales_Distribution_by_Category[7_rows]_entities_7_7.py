
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Region': ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia'],
    'Product A': [20, 40, 30, 10, 15, 20],
    'Product B': [30, 20, 25, 25, 20, 20],
    'Product C': [25, 20, 20, 35, 30, 30],
    'Product D': [25, 20, 25, 30, 35, 30]
}

# Convert data into DataFrame
df = pd.DataFrame(data)
columns = df.columns[1:]

# Create a new figure with specified figure size
plt.figure(figsize=(10, 6))

# Bar width
height = 0.35

# Colors for each stack
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# Starting location for the first bar
y_offset = 0

# Plot bars
for i, col in enumerate(columns):
    plt.barh(y=df['Region'], width=df[col], left=y_offset, height=height, color=colors[i], edgecolor='grey')
    y_offset = y_offset + df[col]

# Display the values on the bars
for xpos, xpos_offset in enumerate(df.index):
    cum_values = 0  # Accumulator for stacked values
    for col in columns:
        value = df.loc[xpos_offset, col]
        if value > 0:  # Only display positive values
            plt.text(cum_values + value/2, xpos, str(value) + '%', ha='center', va='center')
        cum_values += value

# Add labels and title
plt.xlabel('Market Share (%)')
plt.title('Market Share by Region and Product')

# Turn off y ticks, x ticks, x grid
plt.yticks([])
plt.xticks([])
plt.grid(False)

# Display legend
plt.legend(columns, loc='lower right')

# Show the plot
plt.show()