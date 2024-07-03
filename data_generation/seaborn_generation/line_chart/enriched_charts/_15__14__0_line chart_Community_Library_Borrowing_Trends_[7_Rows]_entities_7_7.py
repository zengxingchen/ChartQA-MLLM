
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': list(range(2000, 2022)),
    'Number of International Trips (millions)': [30, 32, 31, 33, 35, 38, 40, 45, 43, 41, 44, 46, 49, 52, 55, 53, 57, 60, 62, 65, 40, 55]
}

df = pd.DataFrame(data)

line_colors = ["#2ca02c"]
plt.figure(figsize=(16, 8))

ax = sns.lineplot(x='Year', y='Number of International Trips (millions)', data=df, color=line_colors[0])

ax.set_title('Annual Number of International Trips from 2000 to 2021')
ax.set_xlabel('Year')
ax.set_ylabel('Number of International Trips (millions)')

ax.annotate('Global Recession', xy=(2009, 41), xytext=(2009, 50),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Pandemic Drop', xy=(2020, 40), xytext=(2020, 50),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Post-Pandemic Recovery', xy=(2021, 55), xytext=(2021, 60),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

plt.show()