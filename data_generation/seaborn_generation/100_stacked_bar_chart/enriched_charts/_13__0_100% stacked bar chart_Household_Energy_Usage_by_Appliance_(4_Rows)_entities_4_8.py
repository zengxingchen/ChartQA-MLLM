
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataframe
data = {
    "Topic": ["Science"]*5 + ["History"]*5 + ["Astronomy"]*5,
    "Category": ["Physics", "Chemistry", "Biology", "Astronomy", "Geology", 
                 "Ancient", "Medieval", "Modern", "Contemporary", "Industrial", 
                 "Planets", "Stars", "Galaxies", "Black Holes", "Space Exploration"],
    "Percentage": [20, 30, 25, 15, 10, 25, 20, 30, 15, 10, 10, 20, 30, 25, 15]
}
df = pd.DataFrame(data)

# Pivot the dataframe to wide format
df_pivot = df.pivot("Category", "Topic", "Percentage")

# Normalize the data as fractions
df_pivot_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0)

# Bar colors
colors = ["#FF6347", "#4682B4", "#8A2BE2"]

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(8, 10))

# Plot the bars vertically (stacked)
bar_sections = []
prev_values = np.zeros(len(df_pivot_normalized))

for i, col in enumerate(df_pivot_normalized.columns):
    values = df_pivot_normalized[col]
    bar_section = plt.bar(df_pivot_normalized.index, values, bottom=prev_values, 
                          color=colors[i], edgecolor='white', width=0.5)
    bar_sections.append(bar_section)
    prev_values += values

# Add a legend and informative axis label
ax.legend(bar_sections, df_pivot_normalized.columns, loc="upper right", title="Topic")
ax.set(ylim=(0, 1), ylabel="Percentage of Interest", xlabel="Category")

# Add percentage values to each section.
for bar in bar_sections:
    for rect in bar:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        label = f"{y_value:.0%}"
        plt.text(x_value, rect.get_y() + y_value / 2, label, va='center', ha='center', color='black')

# Set the title of the chart
plt.title('Distribution of Interest Across Topics')

sns.despine(left=True, bottom=True)

# Display the chart
plt.show()