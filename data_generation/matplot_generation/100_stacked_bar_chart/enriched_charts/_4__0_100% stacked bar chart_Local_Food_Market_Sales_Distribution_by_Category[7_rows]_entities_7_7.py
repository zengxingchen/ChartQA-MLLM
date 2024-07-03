
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Category': ['Fiction', 'Non-Fiction', 'Children', 'Science', 'History', 'Biography', 'Self-Help', 'Comics'],
    'Physical Book': [40, 25, 35, 30, 20, 25, 20, 30],
    'E-book': [30, 35, 20, 25, 40, 30, 30, 25],
    'Audio Book': [20, 25, 30, 35, 30, 35, 40, 30],
    'Other': [10, 15, 15, 10, 10, 10, 10, 15]
}

# Convert data into DataFrame
df = pd.DataFrame(data)
columns = df.columns[1:]

# Create a new figure with specified figure size
plt.figure(figsize=(12, 8))

# Bar width
bar_width = 0.7

# Colors for each stack
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1"]

# Starting location for the first bar
x_offset = 0

# Plot bars
for i, col in enumerate(columns):
    plt.bar(df['Category'], df[col], bottom=x_offset, width=bar_width, color=colors[i], edgecolor='grey')
    x_offset = x_offset + df[col]

# Display the values on the bars
for xpos in range(len(df)):
    cum_values = 0  # Accumulator for stacked values
    for col in columns:
        value = df.loc[xpos, col]
        if value > 0:  # Only display positive values
            plt.text(xpos, cum_values + value/2, str(value) + '%', ha='center', va='center')
        cum_values += value

# Add labels and title
plt.ylabel('Market Share (%)')
plt.title('Market Share by Category and Format', pad=20)

# Turn off x ticks, y ticks, y grid
plt.xticks([])
plt.yticks([])
plt.grid(False)

# Display legend
plt.legend(columns, loc='upper right')

# Show the plot
plt.show()