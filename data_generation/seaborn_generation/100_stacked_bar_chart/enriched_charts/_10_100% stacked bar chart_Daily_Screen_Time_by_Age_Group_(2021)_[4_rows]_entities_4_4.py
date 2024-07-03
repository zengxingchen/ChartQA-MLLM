
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Your input data
data = [
    {'Age Group': '0-8', 'Fruits': 20, 'Vegetables': 25, 'Grains': 30, 'Dairy': 25},
    {'Age Group': '9-18', 'Fruits': 15, 'Vegetables': 35, 'Grains': 25, 'Dairy': 25},
    {'Age Group': '19-34', 'Fruits': 10, 'Vegetables': 30, 'Grains': 40, 'Dairy': 20},
    {'Age Group': '35-50', 'Fruits': 25, 'Vegetables': 20, 'Grains': 35, 'Dairy': 20},
    {'Age Group': '51-65', 'Fruits': 30, 'Vegetables': 15, 'Grains': 35, 'Dairy': 20},
    {'Age Group': '66+', 'Fruits': 25, 'Vegetables': 20, 'Grains': 30, 'Dairy': 25}
]

# Convert into pandas DataFrame
df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

# Calculate the percentage for 100% stacked bar
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.7
categories = df_percentage.index
colors = ['#FF5733', '#33FF57', '#3357FF', '#F7DC6F']

# Initial bottom to stack the bars
bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    # Update the bottom to stack the next layer of bars
    bottom = bottom + df_percentage[col].values

# Beautify the plot
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Food Type Consumption by Age Group')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))

# Display the percentages on the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    if height > 0:  # To avoid clutter, only display if height is significant
        ax.text(x + width / 2,
                y + height / 2,
                f"{height:.1f}%",
                ha='center',
                va='center')

# Show the plot
plt.tight_layout()
plt.show()