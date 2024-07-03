
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Cardio': [40.2, 42.5, 45.0, 47.5, 50.0],
    'Strength': [30.1, 28.9, 27.0, 25.0, 22.5],
    'Flexibility': [20.5, 19.0, 17.0, 15.0, 12.5],
    'High-Intensity': [9.2, 9.6, 11.0, 12.5, 15.0]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(12, 8))  # Adjusting the figure size
df_percentage.plot(kind='bar', stacked=True, width=0.6, color=['#FF7F50', '#6A5ACD', '#2E8B57', '#FF4500'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Exercise Type')
ax.set_xlabel('Year')
ax.set_title('Yearly Distribution of Exercise Types Among Adults (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Exercise Type', loc='upper right', bbox_to_anchor=(1.25, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()