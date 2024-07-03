
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Technology': [30, 35, 40, 45, 50],
    'Healthcare': [25, 20, 15, 10, 10],
    'Education': [20, 25, 30, 25, 20],
    'Environment': [15, 10, 10, 10, 10],
    'Entertainment': [10, 10, 5, 10, 10]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(10, 8))
df_percentage.plot(kind='bar', stacked=True, width=0.6, color=['#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#FFD700'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Research Funding')
ax.set_xlabel('Year')
ax.set_title('Distribution of Research Funding Over the Years (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Research Area', loc='upper left', bbox_to_anchor=(1, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()