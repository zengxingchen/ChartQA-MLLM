
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=24, freq='MS'),
    'Value': [22, 28, 25, 33, 38, 43, 48, 52, 57, 55, 59, 63, 68, 70, 73, 75, 78, 81, 83, 86, 89, 92, 94, 98]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 9))
ax.fill_between(df['Date'], df['Value'], color='#ff7f0e', alpha=0.7)

ax.set_title('Astronomy & Space Exploration: Observations Over Time', fontsize=18, pad=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Observation Count', fontsize=14)
ax.annotate('Significant Increase', xy=(df['Date'].iloc[-1], df['Value'].iloc[-1]), xytext=(df['Date'].iloc[-5], df['Value'].iloc[-1] + 10),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

plt.tight_layout()
plt.show()