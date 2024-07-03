
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataframe
data = {
    "Season": ["Spring"]*5 + ["Summer"]*5 + ["Autumn"]*5 + ["Winter"]*5,
    "Activity": ["Running", "Swimming", "Cycling", "Hiking", "Other"]*4,
    "Percentage": [30, 20, 25, 15, 10, 20, 35, 15, 20, 10, 25, 15, 30, 20, 10, 15, 10, 20, 35, 20]
}
df = pd.DataFrame(data)

# Pivot the dataframe to wide format
df_pivot = df.pivot("Season", "Activity", "Percentage")

# Normalize the data as fractions
df_pivot_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0)

# Bar colors
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(8, 10))

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
ax.legend(bar_sections, df_pivot_normalized.columns, loc="upper right", title="Activities")
ax.set(ylim=(0, 1), xlabel="Season", ylabel="Percentage of Activity Participation")

# Add percentage values to each section
for bar in bar_sections:
    for rect in bar:
        height = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        label = f"{height:.0%}"
        plt.text(x_value, rect.get_y() + height / 2, label, va='center', ha='center', color='black')

# Set the title of the chart
plt.title('Seasonal Activity Participation Distribution', pad=20)

sns.despine(left=True, bottom=True)

# Display the chart
plt.show()