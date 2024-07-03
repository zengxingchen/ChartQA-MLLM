
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
    'Books_Sold': [120, 180, 240, 300, 400, 600, 750, 700, 650, 500, 400, 200, 
                   140, 200, 260, 320, 420, 620, 780, 720, 680, 520, 420, 220]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(16, 8))
ax = sns.lineplot(x='Date', y='Books_Sold', data=df, color='#1f77b4', label='Books Sold')
ax.fill_between(df['Date'], df['Books_Sold'], color='#1f77b4', alpha=0.3)

# Annotations
for index, value in df.iterrows():
    ax.text(value['Date'], value['Books_Sold'], str(value['Books_Sold']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)
    
# Aesthetics
plt.title('Monthly Book Sales Over Two Years', pad=20)
plt.xlabel('Date')
plt.ylabel('Books Sold')
sns.despine(trim=True)

# Display
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()