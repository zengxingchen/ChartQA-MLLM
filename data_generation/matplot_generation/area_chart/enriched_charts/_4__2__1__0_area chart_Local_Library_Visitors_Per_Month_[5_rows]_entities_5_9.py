
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=48, freq='MS'),
    'Value': [22, 28, 25, 33, 38, 43, 48, 52, 57, 55, 59, 63, 68, 70, 73, 75, 78, 81, 83, 86, 89, 92, 94, 98, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 10))
ax.fill_between(df['Date'], df['Value'], color='#1f77b4', alpha=0.7)

ax.set_title('Economics & Finance: Market Growth Over Time', fontsize=20, pad=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Market Value (in Millions)', fontsize=14)
ax.annotate('Peak Growth', xy=(df['Date'].iloc[-1], df['Value'].iloc[-1]), xytext=(df['Date'].iloc[-8], df['Value'].iloc[-1] - 20),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

plt.tight_layout()
plt.show()