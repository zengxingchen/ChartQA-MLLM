
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': list(range(2000, 2022)),
    'Average Temperature': [14.1, 14.2, 14.4, 14.3, 14.5, 14.6, 14.7, 14.8, 14.7, 14.9, 15.0, 15.1, 15.0, 15.2, 15.3, 15.4, 15.5, 15.6, 15.7, 15.8, 15.9, 16.0]
}

df = pd.DataFrame(data)

# Settings for colors and figure size
line_color = "#1f77b4"
plt.figure(figsize=(14, 8))

# Plot the line chart with seaborn
ax = sns.lineplot(x='Year', y='Average Temperature', data=df, color=line_color)

# Add a title and labels
ax.set_title('Annual Average Temperature from 2000 to 2021', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Average Temperature (°C)', fontsize=14)

# Annotate significant data points
ax.annotate('Slight Dip', xy=(2003, 14.3), xytext=(2003, 14.0),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Steady Increase', xy=(2015, 15.4), xytext=(2015, 15.1),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Record High', xy=(2021, 16.0), xytext=(2021, 15.7),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

# Show the plot
plt.show()