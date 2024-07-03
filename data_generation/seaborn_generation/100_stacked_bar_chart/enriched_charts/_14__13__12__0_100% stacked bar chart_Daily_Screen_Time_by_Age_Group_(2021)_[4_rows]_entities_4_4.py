
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'AdventureSports': [22, 25, 28, 30, 32],
    'BeachHolidays': [30, 32, 28, 25, 23],
    'CulturalTours': [18, 20, 22, 25, 27],
    'WildlifeSafaris': [15, 13, 12, 10, 9],
    'CityBreaks': [15, 10, 10, 10, 9]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(12, 10))
df_percentage.plot(kind='bar', stacked=True, width=0.7, color=['#1E90FF', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Travel Preferences')
ax.set_xlabel('Year')
ax.set_title('Travel Preferences Trends Over the Years (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Travel Activity', loc='upper left', bbox_to_anchor=(1, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()