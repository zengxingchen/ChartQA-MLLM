
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data for one year, with a simple pattern
temperature_data = {
    "Day": list(range(1, 366)),
    "Average_Temperature_C": [2.5 + 0.1 * ((i // 30) % 12) for i in range(365)]
}

# Convert the dictionary to a Pandas DataFrame
data = pd.DataFrame(temperature_data)

# Create the area plot
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Define a color palette
palette = sns.color_palette(["#5e81ac", "#bf616a", "#d08770", "#ebcb8b", "#a3be8c", "#b48ead"])

# Generate the area plot
sns.lineplot(data=data, x="Day", y="Average_Temperature_C", palette=palette, linewidth=0)

# Filling the area under the line
plt.fill_between(data["Day"], data["Average_Temperature_C"], color="#5e81ac")

# Add title and labels
plt.title("Average Daily Temperatures Over a Year")
plt.xlabel("Day of the Year")
plt.ylabel("Average Temperature (°C)")

# Add text annotation
plt.text(200, 4, "Peak of Summer", fontsize=12, va='center', ha='center')

plt.show()