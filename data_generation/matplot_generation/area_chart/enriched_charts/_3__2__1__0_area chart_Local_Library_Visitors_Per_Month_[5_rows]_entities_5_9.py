
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=24, freq='MS'),
    'Value': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 10))
ax.fill_between(df['Date'], df['Value'], color='#1f77b4', alpha=0.7)

ax.set_title('Food & Nutrition: Monthly Fruit Consumption', fontsize=20, pad=25)
ax.set_xlabel('Date', fontsize=15)
ax.set_ylabel('Fruit Consumption (kg)', fontsize=15)
ax.annotate('Steady Growth', xy=(df['Date'].iloc[-1], df['Value'].iloc[-1]), xytext=(df['Date'].iloc[-6], df['Value'].iloc[-1] - 30),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=13)

plt.tight_layout()
plt.show()