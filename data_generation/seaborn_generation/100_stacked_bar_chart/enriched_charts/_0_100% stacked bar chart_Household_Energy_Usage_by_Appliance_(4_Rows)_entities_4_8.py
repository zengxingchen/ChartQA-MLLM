
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataframe
data = {
    "Season": ["Spring"]*5 + ["Summer"]*5 + ["Autumn"]*5 + ["Winter"]*5,
    "Fruit": ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]*4,
    "Percentage": [25, 20, 15, 10, 30, 20, 25, 30, 5, 20, 30, 10, 10, 35, 15, 15, 15, 25, 20, 25]
}
df = pd.DataFrame(data)

# Pivot the dataframe to wide format
df_pivot = df.pivot("Season", "Fruit", "Percentage")

# Normalize the data as fractions
df_pivot_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0)

# Bar colors
colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#D1C4E9"]

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 8))

# Plot the bars horizontally (stacked)
bar_sections = []
prev_values = np.zeros(len(df_pivot_normalized))

for i, col in enumerate(df_pivot_normalized.columns):
    values = df_pivot_normalized[col]
    bar_section = plt.barh(df_pivot_normalized.index, values, left=prev_values, 
                           color=colors[i], edgecolor='white', height=0.4)
    bar_sections.append(bar_section)
    prev_values += values

# Add a legend and informative axis label
ax.legend(bar_sections, df_pivot_normalized.columns, loc="lower right", title="Fruits")
ax.set(xlim=(0, 1), ylabel="Season", xlabel="Percentage of Fruit Consumption")

# Add percentage values to each section.
for bar in bar_sections:
    for rect in bar:
        x_value = rect.get_width()
        y_value = rect.get_y() + rect.get_height() / 2
        label = f"{x_value:.0%}"
        plt.text(rect.get_x() + x_value/2, y_value, label, va='center', ha='center', color='black')

# Set the title of the chart
plt.title('Seasonal Fruit Consumption Distribution')

sns.despine(left=True, bottom=True)

# Display the chart
plt.show()