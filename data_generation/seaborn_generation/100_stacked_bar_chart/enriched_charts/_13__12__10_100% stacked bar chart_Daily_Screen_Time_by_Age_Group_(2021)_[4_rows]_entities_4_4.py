
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Your input data
data = [
    {'Age Group': '0-8', 'Vegetables': 25, 'Fruits': 20, 'Proteins': 30, 'Carbs': 25},
    {'Age Group': '9-18', 'Vegetables': 20, 'Fruits': 25, 'Proteins': 35, 'Carbs': 20},
    {'Age Group': '19-34', 'Vegetables': 30, 'Fruits': 20, 'Proteins': 30, 'Carbs': 20},
    {'Age Group': '35-50', 'Vegetables': 35, 'Fruits': 15, 'Proteins': 25, 'Carbs': 25},
    {'Age Group': '51-65', 'Vegetables': 25, 'Fruits': 30, 'Proteins': 20, 'Carbs': 25},
    {'Age Group': '66+', 'Vegetables': 30, 'Fruits': 25, 'Proteins': 20, 'Carbs': 25}
]

# Convert into pandas DataFrame
df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

# Calculate the percentage for 100% stacked bar
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(12, 10))

bar_width = 0.5
categories = df_percentage.index
colors = ['#4CAF50', '#FFEB3B', '#FF5722', '#03A9F4']

# Initial bottom to stack the bars
bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

# Beautify the plot
ax.set_ylabel('Percentage')
ax.set_title('Food Consumption Distribution by Age Group')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

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