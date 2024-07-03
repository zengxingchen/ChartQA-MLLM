
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame from provided data
data = {
    'Year': list(range(2000, 2022)),
    'GDP Growth': [4.1, 0.8, 1.6, 2.8, 3.8, 3.5, 2.9, 1.9, -0.1, -2.5, 2.6,
                   1.6, 2.2, 1.7, 2.6, 2.9, 1.6, 2.4, 2.9, 2.3, -3.5, 5.7]
}

df = pd.DataFrame(data)

# Settings for colors and figure size
line_colors = ["#FF5733", "#C70039"]
plt.figure(figsize=(12, 6))

# Plot the line chart with seaborn
ax = sns.lineplot(x='Year', y='GDP Growth', data=df, palette=line_colors)

# Add a title and labels
ax.set_title('Annual GDP Growth from 2000 to 2021')
ax.set_xlabel('Year')
ax.set_ylabel('GDP Growth (%)')

# Annotate significant data points
ax.annotate('Economic Downturn', xy=(2008, -0.1), xytext=(2008, 1),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Pandemic Impact', xy=(2020, -3.5), xytext=(2020, 0),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Recovery', xy=(2021, 5.7), xytext=(2021, 4),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

# Show the plot
plt.show()