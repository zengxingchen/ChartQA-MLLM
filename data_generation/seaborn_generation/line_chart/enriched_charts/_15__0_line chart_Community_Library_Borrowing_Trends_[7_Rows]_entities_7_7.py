
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame from provided data
data = {
    'Year': list(range(2000, 2022)),
    'CO2 Emissions': [25.4, 26.2, 27.1, 28.3, 29.0, 30.1, 31.5, 32.2, 33.0, 33.5, 34.7,
                      35.8, 36.5, 37.1, 37.7, 38.4, 39.1, 40.0, 40.7, 41.2, 40.0, 41.5]
}

df = pd.DataFrame(data)

# Settings for colors and figure size
line_colors = ["#1f77b4"]
plt.figure(figsize=(14, 7))

# Plot the line chart with seaborn
ax = sns.lineplot(x='Year', y='CO2 Emissions', data=df, color=line_colors[0])

# Add a title and labels
ax.set_title('Annual CO2 Emissions from 2000 to 2021 (Million Metric Tons)')
ax.set_xlabel('Year')
ax.set_ylabel('CO2 Emissions (Million Metric Tons)')

# Annotate significant data points
ax.annotate('Economic Expansion', xy=(2007, 32.2), xytext=(2007, 34),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Financial Crisis Impact', xy=(2009, 33.5), xytext=(2009, 35),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Pandemic Drop', xy=(2020, 40.0), xytext=(2020, 38),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

# Show the plot
plt.show()