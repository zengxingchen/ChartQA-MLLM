
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=24, freq='MS'),
    'Index': [1500, 1520, 1480, 1530, 1570, 1600, 1625, 1610, 1650, 1700, 1675, 1720,
              1750, 1780, 1800, 1830, 1850, 1900, 1920, 1950, 1980, 2000, 2025, 2050]
}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
plt.fill_between(df['Date'], df['Index'], color='#4682B4', alpha=0.7)
plt.plot(df['Date'], df['Index'], color='#1E90FF', alpha=0.9)

# Headline and labels
plt.title('Stock Market Index Over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Index Value', fontsize=14)

# Annotation
max_value = df['Index'].max()
max_date = df['Date'][df['Index'].idxmax()]
plt.annotate(f'Max: {max_value}', xy=(max_date, max_value), xytext=(max_date, max_value+100),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()