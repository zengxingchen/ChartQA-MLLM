
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': list(range(2000, 2022)),
    'Space Missions': [2, 3, 4, 6, 5, 7, 8, 9, 10, 8, 9, 11, 12, 13, 14, 15, 14, 16, 17, 19, 18, 20]
}

df = pd.DataFrame(data)

# Settings for colors and figure size
line_colors = ["#3498db", "#2ecc71"]
plt.figure(figsize=(14, 8))

# Plot the line chart with seaborn
ax = sns.lineplot(x='Year', y='Space Missions', data=df, color="#3498db")

# Add a title and labels
ax.set_title('Annual Space Missions from 2000 to 2021', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Missions', fontsize=14)

# Annotate significant data points
ax.annotate('Surge in Missions', xy=(2013, 13), xytext=(2013, 10),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Decrease in Missions', xy=(2020, 18), xytext=(2020, 15),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Peak Missions', xy=(2021, 20), xytext=(2021, 17),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

# Show the plot
plt.show()