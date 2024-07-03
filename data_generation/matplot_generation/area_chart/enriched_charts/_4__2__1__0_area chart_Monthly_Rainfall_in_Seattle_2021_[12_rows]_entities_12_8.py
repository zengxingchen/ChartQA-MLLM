
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': pd.date_range(start='2024-01-01', periods=36, freq='M').strftime('%Y-%m').tolist(),
    'Monthly_Revenue': [
        1500, 1600, 1550, 1650, 1700, 1750, 1850, 1900, 2000, 2100, 
        2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 
        3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 
        4200, 4300, 4400, 4500, 4600, 4700
    ]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 7))

ax.fill_between(df['Date'], df['Monthly_Revenue'], color='#1f77b4', alpha=0.6)

ax.set_title('Monthly Revenue Growth Over Three Years', fontsize=18, pad=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Monthly Revenue', fontsize=14)
ax.annotate('Significant Increase', xy=('2025-06', 2900), xytext=('2025-01', 3200),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

ax.spines['top'].set_color('#DDDDDD')
ax.spines['right'].set_color('#DDDDDD')
ax.spines['left'].set_color('#333333')
ax.spines['bottom'].set_color('#333333')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()