
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataframe
data = {
    "Country": ["USA"]*5 + ["UK"]*5 + ["Germany"]*5 + ["Japan"]*5 + ["Australia"]*5,
    "Genre": ["Rock", "Hip-Hop", "Pop", "Jazz", "Classical"]*5,
    "Percentage": [30, 25, 20, 15, 10, 35, 20, 25, 10, 10, 25, 30, 20, 15, 10, 20, 15, 30, 25, 10, 30, 25, 20, 15, 10]
}
df = pd.DataFrame(data)

# Pivot the dataframe to wide format
df_pivot = df.pivot("Country", "Genre", "Percentage")

# Normalize the data as fractions
df_pivot_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0)

# Bar colors
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 8))

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
ax.legend(bar_sections, df_pivot_normalized.columns, loc="upper left", title="Genres")
ax.set(ylim=(0, 1), xlabel="Country", ylabel="Percentage of Music Genre Preference")

# Add percentage values to each section
for bar in bar_sections:
    for rect in bar:
        height = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        label = f"{height:.0%}"
        plt.text(x_value, rect.get_y() + height / 2, label, va='center', ha='center', color='black')

# Set the title of the chart
plt.title('Music Genre Preferences by Country', pad=20)

sns.despine(left=True, bottom=True)

# Display the chart
plt.show()