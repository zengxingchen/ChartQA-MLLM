
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'TV': [35.0, 33.0, 30.0, 28.0, 25.0],
    'Streaming': [25.0, 28.0, 30.0, 32.0, 35.0],
    'Social Media': [20.0, 22.0, 25.0, 28.0, 30.0],
    'Games': [20.0, 17.0, 15.0, 12.0, 10.0]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(10, 6))  # Adjusting the figure size
df_percentage.plot(kind='bar', stacked=True, width=0.5, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Media Consumption')
ax.set_xlabel('Year')
ax.set_title('Yearly Distribution of Different Types of Media Consumption (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Media Type', loc='upper right', bbox_to_anchor=(1.25, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()