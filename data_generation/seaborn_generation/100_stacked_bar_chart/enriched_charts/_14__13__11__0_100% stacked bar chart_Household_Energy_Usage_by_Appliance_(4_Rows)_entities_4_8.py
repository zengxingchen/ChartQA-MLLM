
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataframe
data = {
    "Category": ["Fruits"]*4 + ["Vegetables"]*4 + ["Grains"]*4 + ["Proteins"]*4,
    "Item": ["Consumption", "Nutrition", "Cost", "Availability"]*4,
    "Percentage": [35, 25, 20, 20, 30, 30, 25, 15, 40, 20, 30, 10, 25, 35, 20, 20]
}
df = pd.DataFrame(data)

# Pivot the dataframe to wide format
df_pivot = df.pivot("Category", "Item", "Percentage")

# Normalize the data as fractions
df_pivot_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0)

# Bar colors
colors = ["#4c72b0", "#dd8452", "#55a868", "#c44e52"]

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 9))

# Plot the bars vertically (stacked)
bar_sections = []
prev_values = np.zeros(len(df_pivot_normalized))

for i, col in enumerate(df_pivot_normalized.columns):
    values = df_pivot_normalized[col]
    bar_section = plt.bar(df_pivot_normalized.index, values, bottom=prev_values, 
                          color=colors[i], edgecolor='white', width=0.6)
    bar_sections.append(bar_section)
    prev_values += values

# Add a legend and informative axis label
ax.legend(bar_sections, df_pivot_normalized.columns, loc="upper right", title="Factors")
ax.set(ylim=(0, 1), xlabel="Food Category", ylabel="Percentage of Focus")

# Add percentage values to each section.
for bar in bar_sections:
    for rect in bar:
        height = rect.get_height()
        y_value = rect.get_y() + height / 2
        label = f"{height:.0%}"
        plt.text(rect.get_x() + rect.get_width() / 2, y_value, label, va='center', ha='center', color='black')

# Set the title of the chart
plt.title('Focus on Different Factors by Food Category', pad=20)

sns.despine(left=True, bottom=True)

# Display the chart
plt.show()