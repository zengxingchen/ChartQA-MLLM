
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': list(range(2000, 2022)),
    'GDP Growth Rate': [2.5, 1.1, 1.8, 2.7, 3.4, 3.1, 2.9, 2.3, 0.1, -2.8, 2.5, 1.6, 2.2, 1.7, 2.4, 2.9, 1.5, 2.3, 2.9, 2.2, -3.5, 5.7]
}

df = pd.DataFrame(data)

# Settings for colors and figure size
line_color = "#FF5733"
plt.figure(figsize=(16, 10))

# Plot the line chart with seaborn
ax = sns.lineplot(x='Year', y='GDP Growth Rate', data=df, color=line_color)

# Add a title and labels
ax.set_title('Annual GDP Growth Rate from 2000 to 2021', fontsize=18)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('GDP Growth Rate (%)', fontsize=14)

# Annotate significant data points
ax.annotate('Recession', xy=(2009, -2.8), xytext=(2009, -5),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Sharp Decline', xy=(2020, -3.5), xytext=(2020, -6),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Strong Recovery', xy=(2021, 5.7), xytext=(2021, 3),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

# Show the plot
plt.show()