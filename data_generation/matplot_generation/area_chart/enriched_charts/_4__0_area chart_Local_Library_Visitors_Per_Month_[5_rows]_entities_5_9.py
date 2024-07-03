
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Revenue': [
        1200, 1500, 1300, 1700, 1650, 1400, 1550, 1600, 1750, 1800, 
        1900, 2000, 2100, 1850, 1950, 2050, 2150, 2250, 2200, 2300, 
        2400, 2500, 2350, 2450, 2600, 2550, 2700, 2750, 2800, 2900
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
sns.lineplot(data=df, x='Date', y='Revenue', color="#1E90FF")
plt.fill_between(df.Date, df.Revenue, color="#1E90FF", alpha=0.3)

for index, value in df.iterrows():
    if index % 5 == 0:
        plt.text(value['Date'], value['Revenue'] + 50, f"${value['Revenue']}", ha='center')

plt.title('Daily Revenue in January 2023', y=1.05)
plt.xlabel('Date')
plt.ylabel('Revenue (in USD)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()