
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataframe
data = {
    "Category": ["Startup"]*4 + ["Enterprise"]*4 + ["SME"]*4 + ["Freelancer"]*4,
    "Item": ["Marketing", "Development", "Operations", "Sales"]*4,
    "Percentage": [20, 40, 25, 15, 10, 30, 35, 25, 15, 25, 30, 30, 25, 25, 10, 40]
}
df = pd.DataFrame(data)

# Pivot the dataframe to wide format
df_pivot = df.pivot("Category", "Item", "Percentage")

# Normalize the data as fractions
df_pivot_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0)

# Bar colors
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 10))

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
ax.legend(bar_sections, df_pivot_normalized.columns, loc="upper right", title="Items")
ax.set(ylim=(0, 1), xlabel="Category", ylabel="Percentage of Resource Allocation")

# Add percentage values to each section.
for bar in bar_sections:
    for rect in bar:
        height = rect.get_height()
        y_value = rect.get_y() + height / 2
        label = f"{height:.0%}"
        plt.text(rect.get_x() + rect.get_width() / 2, y_value, label, va='center', ha='center', color='black')

# Set the title of the chart
plt.title('Resource Allocation in Different Business Types', pad=20)

sns.despine(left=True, bottom=True)

# Display the chart
plt.show()