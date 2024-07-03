
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
    'Subscribers': [120, 135, 150, 165, 180, 200, 220, 240, 260, 280, 300, 320, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(14, 7))
ax = sns.lineplot(x='Date', y='Subscribers', data=df, color='#FF6347', label='Subscribers Count')
ax.fill_between(df['Date'], df['Subscribers'], color='#FF6347', alpha=0.3)

# Annotations
for index, value in df.iterrows():
    ax.text(value['Date'], value['Subscribers'], str(value['Subscribers']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)

# Aesthetics
plt.title('Monthly Subscribers Growth Over Two Years', fontsize=16, pad=20)
plt.xlabel('Date')
plt.ylabel('Subscribers Count')
sns.despine(trim=True)

# Display
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()