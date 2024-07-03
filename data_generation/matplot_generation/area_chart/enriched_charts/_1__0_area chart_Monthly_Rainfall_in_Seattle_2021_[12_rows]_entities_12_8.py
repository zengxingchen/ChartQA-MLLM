
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=36, freq='M').strftime('%Y-%m').tolist(),
    'Popularity': [50, 55, 60, 70, 65, 75, 80, 85, 90, 95, 85, 80, 75, 70, 65, 60, 55, 50, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 95, 90, 85, 80, 75, 70]
}

df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(14, 7))

ax.fill_between(df['Date'], df['Popularity'], color='#1f77b4', alpha=0.6)

# Add labels
ax.set_title('Trends in Fashion Popularity Over Time', fontsize=16)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Popularity', fontsize=12)
ax.annotate('Peak Popularity', xy=('2026-06', 100), xytext=('2025-12', 110),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Customize the color scheme
ax.spines['top'].set_color('#CCCCCC')
ax.spines['right'].set_color('#CCCCCC')
ax.spines['left'].set_color('#444444')
ax.spines['bottom'].set_color('#444444')

# Rotate date labels
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()