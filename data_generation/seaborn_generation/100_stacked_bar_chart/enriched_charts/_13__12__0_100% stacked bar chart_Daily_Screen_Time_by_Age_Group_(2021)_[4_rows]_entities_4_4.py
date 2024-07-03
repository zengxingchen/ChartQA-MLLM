
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'PhysicalActivity': [30, 35, 32, 40, 38],
    'HealthyEating': [25, 28, 30, 35, 37],
    'RegularCheckups': [20, 18, 22, 15, 14],
    'MentalWellbeing': [15, 12, 10, 8, 7],
    'Medication': [10, 7, 6, 2, 4]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(10, 8))
df_percentage.plot(kind='bar', stacked=True, width=0.6, color=['#FF4500', '#00BFFF', '#3CB371', '#FFD700', '#800080'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Health Activities')
ax.set_xlabel('Year')
ax.set_title('Health Activities Trends Over the Years (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Health Activity', loc='upper left', bbox_to_anchor=(1, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()