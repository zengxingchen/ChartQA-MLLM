
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=36, freq='MS'),
    'Emissions': [500, 520, 480, 530, 570, 600, 625, 610, 650, 700, 675, 720,
                  750, 780, 800, 830, 850, 900, 920, 950, 980, 1000, 1025, 1050,
                  1080, 1100, 1130, 1150, 1180, 1200, 1225, 1250, 1275, 1300, 1325, 1350]
}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
plt.fill_between(df['Date'], df['Emissions'], color='#2E8B57', alpha=0.6)
plt.plot(df['Date'], df['Emissions'], color='#006400', alpha=0.9)

# Headline and labels
plt.title('Greenhouse Gas Emissions Over Time', fontsize=20, loc='center')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Emissions (in million metric tons)', fontsize=14)

# Annotation
max_value = df['Emissions'].max()
max_date = df['Date'][df['Emissions'].idxmax()]
plt.annotate(f'Max Emissions: {max_value}', xy=(max_date, max_value), xytext=(max_date, max_value+100),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

plt.tight_layout()
plt.show()