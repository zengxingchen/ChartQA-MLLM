
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=36, freq='M').strftime('%Y-%m').tolist(),
    'Revenue_Growth': [
        1500, 1550, 1600, 1800, 1750, 1850, 1900, 1950, 2000, 2100, 
        2150, 2200, 2250, 2300, 2350, 2450, 2500, 2600, 2700, 2800, 
        2850, 2900, 3000, 3100, 3150, 3200, 3300, 3400, 3500, 3600, 
        3700, 3800, 3850, 3900, 4000, 4100
    ]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(18, 10))

ax.fill_between(df['Date'], df['Revenue_Growth'], color='#1f77b4', alpha=0.6)

ax.set_title('Monthly Revenue Growth Over Three Years', fontsize=20, pad=20)
ax.set_xlabel('Date', fontsize=16)
ax.set_ylabel('Revenue Growth', fontsize=16)
ax.annotate('Significant Growth Phase', xy=('2025-06', 2600), xytext=('2025-01', 2800),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=14)

ax.spines['top'].set_color('#DDDDDD')
ax.spines['right'].set_color('#DDDDDD')
ax.spines['left'].set_color('#333333')
ax.spines['bottom'].set_color('#333333')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()