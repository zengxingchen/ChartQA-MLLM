
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Math': [35, 30, 25, 20, 25],
    'Science': [25, 30, 35, 30, 25],
    'History': [20, 20, 25, 30, 25],
    'Art': [20, 20, 15, 20, 25]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(8, 12))
df_percentage.plot(kind='bar', stacked=True, width=0.6, color=['#3498db', '#e74c3c', '#2ecc71', '#9b59b6'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Subjects Chosen')
ax.set_xlabel('Year')
ax.set_title('Yearly Distribution of Subjects Chosen by Students (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Subject', loc='upper right', bbox_to_anchor=(1.3, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()