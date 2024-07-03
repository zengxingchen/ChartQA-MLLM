
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Primary_Education': [60, 55, 50, 45, 40],
    'Secondary_Education': [20, 25, 30, 35, 40],
    'Higher_Education': [15, 15, 15, 15, 15],
    'Technical_Education': [5, 5, 5, 5, 5]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(8, 10))
df_percentage.plot(kind='bar', stacked=True, width=0.6, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Education Levels')
ax.set_xlabel('Year')
ax.set_title('Yearly Distribution of Education Levels (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Education Level', loc='upper right', bbox_to_anchor=(1.3, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()