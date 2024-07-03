
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Poetry': [40, 35, 30, 25, 20],
    'Novels': [30, 25, 20, 35, 30],
    'Essays': [20, 25, 30, 25, 25],
    'Short Stories': [10, 15, 20, 15, 25]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(10, 6))
df_percentage.plot(kind='bar', stacked=True, width=0.7, color=['#FF6347', '#4682B4', '#8A2BE2', '#3CB371'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Genres Chosen')
ax.set_xlabel('Year')
ax.set_title('Yearly Distribution of Literary Genres Chosen by Students (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Genre', loc='upper right', bbox_to_anchor=(1.25, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()