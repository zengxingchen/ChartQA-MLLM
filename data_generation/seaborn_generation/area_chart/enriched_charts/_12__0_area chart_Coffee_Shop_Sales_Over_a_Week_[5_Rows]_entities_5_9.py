
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
    'Stock_Price': [150, 155, 160, 158, 165, 170, 172, 175, 180, 178, 185, 190, 
                    192, 195, 198, 200, 205, 210, 215, 220, 225, 230, 235, 240]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(14, 8))
ax = sns.lineplot(x='Date', y='Stock_Price', data=df, color='#ff5733', label='Stock Price (USD)')
ax.fill_between(df['Date'], df['Stock_Price'], color='#ff5733', alpha=0.3)

# Annotations
for index, value in df.iterrows():
    ax.text(value['Date'], value['Stock_Price'], str(value['Stock_Price']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)
    
# Aesthetics
plt.title('Monthly Average Stock Prices Over Two Years', pad=20)
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
sns.despine(trim=True)

# Display
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()