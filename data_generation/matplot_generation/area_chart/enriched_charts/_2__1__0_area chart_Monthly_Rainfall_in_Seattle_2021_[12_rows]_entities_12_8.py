
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=36, freq='M').strftime('%Y-%m').tolist(),
    'Subscriber_Growth': [
        1000, 1050, 1200, 1400, 1300, 1350, 1600, 1700, 1800, 1900, 
        1850, 2000, 2100, 2200, 2250, 2300, 2350, 2500, 2600, 2700, 
        2800, 2900, 2850, 3000, 3100, 3200, 3300, 3400, 3350, 3500, 
        3600, 3700, 3800, 3900, 4000, 3950
    ]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 8))

ax.fill_between(df['Date'], df['Subscriber_Growth'], color='#ff7f0e', alpha=0.6)

ax.set_title('Monthly Subscriber Growth Over Three Years', fontsize=18, pad=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Subscriber Growth', fontsize=14)
ax.annotate('Rapid Growth Phase', xy=('2025-06', 2500), xytext=('2025-01', 2700),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

ax.spines['top'].set_color('#DDDDDD')
ax.spines['right'].set_color('#DDDDDD')
ax.spines['left'].set_color('#333333')
ax.spines['bottom'].set_color('#333333')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()