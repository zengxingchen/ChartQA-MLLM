
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Rock': [15, 20, 18, 25, 20, 15, 10, 20],
    'Pop': [25, 20, 22, 20, 30, 25, 20, 25],
    'Jazz': [20, 25, 20, 15, 10, 20, 25, 15],
    'Hip-Hop': [10, 15, 10, 15, 20, 20, 25, 20],
    'Classical': [20, 15, 25, 15, 10, 10, 10, 15],
    'Electronic': [10, 5, 5, 10, 10, 10, 10, 5]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 10))

years = df['Year']
categories = ['Rock', 'Pop', 'Jazz', 'Hip-Hop', 'Classical', 'Electronic']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33', '#C70039']

bottom = [0] * len(df)
for category, color in zip(categories, colors):
    values = df[category]
    ax.bar(years, values, bottom=bottom, label=category, color=color, width=0.8)
    bottom = [i+j for i, j in zip(bottom, values)]

ax.set_title('Music Genre Popularity (2015-2022)', fontsize=16, pad=20)
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Year')
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

plt.tight_layout()
plt.show()