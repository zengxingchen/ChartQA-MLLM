
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Research': [55, 50, 45, 40, 35],
    'Development': [20, 25, 30, 35, 40],
    'Marketing': [15, 15, 15, 15, 15],
    'Operations': [10, 10, 10, 10, 10]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(12, 6))
df_percentage.plot(kind='bar', stacked=True, width=0.5, color=['#FF4500', '#1E90FF', '#32CD32', '#8A2BE2'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Activities')
ax.set_xlabel('Year')
ax.set_title('Annual Allocation of Business Activities (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Activity', loc='upper right', bbox_to_anchor=(1.15, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()