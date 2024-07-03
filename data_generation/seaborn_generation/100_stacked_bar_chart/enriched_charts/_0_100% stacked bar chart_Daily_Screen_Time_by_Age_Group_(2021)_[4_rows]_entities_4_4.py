
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Gasoline': [55.5, 50.8, 46.3, 42.9, 38.6],
    'Diesel': [32.5, 30.5, 27.4, 22.9, 19.3],
    'Electric': [5, 7.2, 10.5, 15.3, 21.4],
    'Hybrid': [7, 11.5, 15.8, 18.9, 20.7]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(10, 6))
df_percentage.plot(kind='bar', stacked=True, width=0.7, color=['#FFA07A', '#20B2AA', '#778899', '#9370DB'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Car Sales')
ax.set_xlabel('Year')
ax.set_title('Yearly Car Sales Breakdown by Fuel Type (2018-2022)')
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Fuel Type', loc='upper left', bbox_to_anchor=(1, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()