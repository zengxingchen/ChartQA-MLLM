
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
    'Pageviews': [1200, 1500, 1800, 2200, 2600, 3000, 3400, 3600, 3200, 2800,
                  2400, 2000, 1600, 1400, 1700, 2100, 2500, 2900, 3300, 3500,
                  3100, 2700, 2300, 1900]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(14, 7))
ax = sns.lineplot(x='Date', y='Pageviews', data=df, color='#FF5733', label='Pageviews')
ax.fill_between(df['Date'], df['Pageviews'], color='#FF5733', alpha=0.3)

# Annotations
for index, value in df.iterrows():
    ax.text(value['Date'], value['Pageviews'], str(value['Pageviews']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)
    
# Aesthetics
plt.title('Monthly Pageviews Over Two Years')
plt.xlabel('Date')
plt.ylabel('Pageviews')
sns.despine(trim=True)

# Display
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()