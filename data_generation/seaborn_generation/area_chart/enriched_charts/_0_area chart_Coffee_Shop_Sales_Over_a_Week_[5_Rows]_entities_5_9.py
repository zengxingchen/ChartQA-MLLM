
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
    'Temperature': [5, 7, 10, 13, 17, 20, 22, 21, 18, 14, 10, 6, 4, 6, 11, 14, 18, 21, 23, 22, 19, 15, 11, 7]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(12, 6))
ax = sns.lineplot(x='Date', y='Temperature', data=df, color='#1f77b4', label='Temperature (°C)')
ax.fill_between(df['Date'], df['Temperature'], color='#1f77b4', alpha=0.3)

# Annotations
for index, value in df.iterrows():
    ax.text(value['Date'], value['Temperature'], str(value['Temperature']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)
    
# Aesthetics
plt.title('Monthly Average Temperature Over Two Years')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
sns.despine(trim=True)

# Display
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()