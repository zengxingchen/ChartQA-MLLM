
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
    'Arrivals': [150, 200, 350, 500, 750, 1200, 1700, 1600, 1400, 1100, 800, 400, 
                 180, 220, 380, 520, 780, 1250, 1750, 1650, 1450, 1150, 820, 420]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(14, 7))
ax = sns.lineplot(x='Date', y='Arrivals', data=df, color='#ff6347', label='Tourist Arrivals')
ax.fill_between(df['Date'], df['Arrivals'], color='#ff6347', alpha=0.3)

# Annotations
for index, value in df.iterrows():
    ax.text(value['Date'], value['Arrivals'], str(value['Arrivals']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)
    
# Aesthetics
plt.title('Monthly Tourist Arrivals Over Two Years', pad=20)
plt.xlabel('Date')
plt.ylabel('Arrivals')
sns.despine(trim=True)

# Display
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()