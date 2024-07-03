
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01',
             '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01',
             '2021-11-01', '2021-12-01', '2022-01-01', '2022-02-01', '2022-03-01',
             '2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01',
             '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01'],
    'Revenue': [2500, 2700, 3000, 3500, 4000, 4500, 4700, 4200, 3800, 3400,
                3000, 2600, 2200, 2400, 2700, 3200, 3700, 4200, 4400, 3900,
                3500, 3100, 2700, 2300]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(16, 8))
ax = sns.lineplot(x='Date', y='Revenue', data=df, color='#1f77b4', label='Revenue')
ax.fill_between(df['Date'], df['Revenue'], color='#1f77b4', alpha=0.3)

# Annotations
for index, value in df.iterrows():
    ax.text(value['Date'], value['Revenue'], str(value['Revenue']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)

# Aesthetics
plt.title('Monthly Sales Revenue Over Two Years', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Revenue')
sns.despine(trim=True)

# Display
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()