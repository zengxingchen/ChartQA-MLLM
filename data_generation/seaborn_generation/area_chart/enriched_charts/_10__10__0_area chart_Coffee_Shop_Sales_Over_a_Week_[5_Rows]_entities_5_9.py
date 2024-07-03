
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
    'Distance': [15, 18, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(16, 8))
ax = sns.lineplot(x='Date', y='Distance', data=df, color='#2E8B57', label='Distance Traveled (km)')
ax.fill_between(df['Date'], df['Distance'], color='#2E8B57', alpha=0.3)

# Annotations
for index, value in df.iterrows():
    ax.text(value['Date'], value['Distance'], str(value['Distance']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)

# Aesthetics
plt.title('Monthly Distance Traveled Over Two Years', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Distance Traveled (km)')
sns.despine(trim=True)

# Display
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()