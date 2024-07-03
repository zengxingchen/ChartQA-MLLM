
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data Preparation
data = {
    'Date': pd.date_range(start='2024-01-01', periods=24, freq='MS'),
    'Value': [25, 30, 28, 35, 40, 45, 50, 55, 60, 58, 62, 65, 70, 72, 75, 78, 80, 82, 85, 87, 90, 93, 95, 100]
}
df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
ax.fill_between(df['Date'], df['Value'], color='#1f77b4', alpha=0.6)

# Adding Labels and Title
ax.set_title('Future Technologies & Society: Value Over Time', fontsize=16, pad=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Value', fontsize=14)
ax.annotate('Peak Value', xy=(df['Date'].iloc[-1], df['Value'].iloc[-1]), xytext=(df['Date'].iloc[-6], df['Value'].iloc[-1] + 10),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()