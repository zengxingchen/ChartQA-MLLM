
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=24, freq='MS'),
    'Value': [10, 15, 13, 17, 22, 27, 23, 29, 35, 33, 37, 40, 45, 48, 50, 52, 55, 58, 60, 62, 65, 68, 70, 75]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 10))
ax.fill_between(df['Date'], df['Value'], color='#FF6347', alpha=0.6)

ax.set_title('Music & Performing Arts: Popularity Over Time', fontsize=18, pad=25)
ax.set_xlabel('Date', fontsize=15)
ax.set_ylabel('Popularity Index', fontsize=15)
ax.annotate('Significant Rise', xy=(df['Date'].iloc[12], df['Value'].iloc[12]), xytext=(df['Date'].iloc[7], df['Value'].iloc[12] + 15),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=13)

plt.tight_layout()
plt.show()