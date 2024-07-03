
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': list(range(2000, 2022)),
    'Marathon Participants': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2700, 2800, 2900, 3000, 3200, 3300, 3400, 3500, 3600, 3000, 3700]
}

df = pd.DataFrame(data)

# Settings for colors and figure size
line_colors = ["#ff5733", "#33ff57"]
plt.figure(figsize=(12, 7))

# Plot the line chart with seaborn
ax = sns.lineplot(x='Year', y='Marathon Participants', data=df, color="#ff5733")

# Add a title and labels
ax.set_title('Annual Marathon Participation from 2000 to 2021', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Participants', fontsize=14)

# Annotate significant data points
ax.annotate('Steady Increase', xy=(2015, 3200), xytext=(2015, 2900),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Pandemic Impact', xy=(2020, 3000), xytext=(2020, 3300),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Record Participation', xy=(2021, 3700), xytext=(2021, 3400),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

# Show the plot
plt.show()