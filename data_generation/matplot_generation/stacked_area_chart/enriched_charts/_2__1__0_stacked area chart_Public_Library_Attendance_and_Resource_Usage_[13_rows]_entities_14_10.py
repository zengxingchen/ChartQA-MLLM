
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Quarter': [
        'Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 
        'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
        'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'
    ],
    'Stocks': [5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200],
    'Bonds': [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100],
    'Commodities': [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100]
}

df = pd.DataFrame(data)

# Figure and Plot
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(df['Quarter'], df['Stocks'], df['Bonds'], df['Commodities'],
             labels=['Stocks', 'Bonds', 'Commodities'],
             colors=['#ff9999', '#66b3ff', '#99ff99'])

# Title and labels
plt.title('Quarterly Investment Portfolio Breakdown', pad=30)
plt.xlabel('Quarter')
plt.ylabel('Investment Value (in $1000s)')
plt.legend(loc='upper left')

# Annotations
for i, (quarter, stocks, bonds, commodities) in enumerate(zip(df['Quarter'], df['Stocks'], df['Bonds'], df['Commodities'])):
    total_value = stocks + bonds + commodities
    ax.annotate(f'Total: {total_value}', (i, total_value), textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.tight_layout()
plt.show()