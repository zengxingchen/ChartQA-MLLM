
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
data = [
    {'Age Group': 'Young Adults', 'Water Pollution': 15, 'Deforestation': 35, 'Climate Change': 25, 'Plastic Waste': 25},
    {'Age Group': 'Adults', 'Water Pollution': 20, 'Deforestation': 25, 'Climate Change': 30, 'Plastic Waste': 25},
    {'Age Group': 'Middle-Aged', 'Water Pollution': 30, 'Deforestation': 20, 'Climate Change': 25, 'Plastic Waste': 25},
    {'Age Group': 'Seniors', 'Water Pollution': 35, 'Deforestation': 10, 'Climate Change': 20, 'Plastic Waste': 35},
    {'Age Group': 'Elderly', 'Water Pollution': 25, 'Deforestation': 15, 'Climate Change': 20, 'Plastic Waste': 40}
]

df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

# Calculate percentage
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 12))  # Modified the size for a better vertical layout

bar_width = 0.5  # Reduced bar width for clarity
categories = df_percentage.index
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Updated color scheme

bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

# Labels and title
ax.set_ylabel('Percentage')
ax.set_xlabel('Age Group')
ax.set_title('Concerns About Environmental Issues by Age Group', pad=40)  # Adjusted title position for better layout
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Changed legend position to avoid overlap

# Adding percentage labels
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    if height > 0:
        ax.text(x + width / 2,
                y + height / 2,
                f"{height:.1f}%",
                ha='center',
                va='center')

plt.tight_layout()
plt.show()