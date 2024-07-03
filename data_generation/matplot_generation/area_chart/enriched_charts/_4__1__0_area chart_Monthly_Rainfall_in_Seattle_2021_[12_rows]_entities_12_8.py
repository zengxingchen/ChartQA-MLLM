
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=44, freq='M').strftime('%Y-%m').tolist(),
    'Innovation Index': [45, 47, 50, 55, 60, 62, 65, 70, 68, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95, 97, 99, 100, 98, 95, 92, 90, 88, 85, 83, 80, 78, 75, 73, 70, 68, 65, 62, 60, 58, 55, 52, 50, 48, 45]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 8))

ax.fill_between(df['Date'], df['Innovation Index'], color='#FF5733', alpha=0.6)

ax.set_title('Innovation Index Trends Over Time', fontsize=18, pad=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Innovation Index', fontsize=14)
ax.annotate('Peak Innovation', xy=('2025-10', 100), xytext=('2025-04', 105),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

ax.spines['top'].set_color('#E0E0E0')
ax.spines['right'].set_color('#E0E0E0')
ax.spines['left'].set_color('#555555')
ax.spines['bottom'].set_color('#555555')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()